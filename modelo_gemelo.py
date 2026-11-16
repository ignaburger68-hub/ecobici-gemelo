"""
modelo_gemelo.py - Modelo de eventos discretos del gemelo digital Ecobici

Funciones del planteamiento:
  Función 1  Gemelo.tasas()          tasas lambda (retiros) y mu (devoluciones) por bloque de 15 min
  Función 2  simular()               regla de transición de cada estación, evento por evento
  Función 3  Gemelo.pronosticar()    probabilidad de quedar vacía / llena (simulación)
             prob_exacta()           la misma probabilidad con la cadena de Markov (validación)
  Función 4  Gemelo.planificar()     plan del camión: voraz con g_i(Delta) vs regla umbral vs nada
  Referencia Gemelo.sin_resincronizar_dia()   mismo modelo calibrado una vez, desde las 06:00

Unidades: tiempo de simulación en minutos desde t0; tasas en eventos por hora.
"""
import json
import os

import numpy as np
import pandas as pd

import config_gemelo as cfg
from datos_gemelo import (Panel, bloque_de, buscar_viajes, dias_historia, es_habil, estado_en_vivo,
                          factores_por_hora, leer_clima, leer_estaciones, leer_feed, leer_perfil_guardado,
                          leer_viajes, perfil_base, pronostico_clima_en_vivo, tabla_factores_clima, tipo_idx)

H = cfg.HORIZONTE_MIN
K_BLOQUES = H // 15
FIN = np.float32(H + 1e-3)


# =====================================================================
# Generación de la demanda (exógena: no depende del estado -> CRN exactos)
# =====================================================================
def generar_eventos(lam, mu, R, rng, phi=0.0, cambios=None):
    """
    lam, mu: (I, K) tasas por hora en K bloques de 15 min.
    phi > 0: multiplicador del día G_r ~ Gamma(media 1, varianza phi), común a las estaciones.
    cambios: lista de (minuto, delta (I,)) = traslados del camión en ese instante.
    Devuelve dict con t (N, I, R) minutos ordenados, tipo (N, I, R): -1 retiro, +1 devolución,
    0 relleno, 10+k camión k; y deltas (I, n_cambios).
    """
    I, K = lam.shape
    G = rng.gamma(1 / phi, phi, R) if phi and phi > 0 else np.ones(R)
    tasa = np.concatenate([lam, mu], axis=1)                         # (I, 2K): retiros y luego devoluciones
    cnt = rng.poisson(np.maximum(tasa, 0)[:, None, :] * G[None, :, None] * 0.25)   # 15 min = 0.25 h
    cum = cnt.cumsum(-1)
    n_max = max(int(cum[..., -1].max()), 1)
    j = np.arange(n_max)
    cat = (j[None, None, :, None] >= cum[:, :, None, :]).sum(-1)    # categoría de cada casilla
    relleno = cat >= 2 * K
    bloque = cat % K
    u = rng.random((I, R, n_max), dtype=np.float32)
    t = (15 * bloque + 15 * u).astype(np.float32)
    tipo = np.where(cat < K, -1, 1).astype(np.int8)
    t[relleno] = np.inf
    tipo[relleno] = 0
    deltas = None
    if cambios:
        extra_t = [np.full((I, R, 1), tau, np.float32) for tau, _ in cambios]
        extra_k = [np.full((I, R, 1), 10 + k, np.int8) for k in range(len(cambios))]
        t = np.concatenate([t] + extra_t, axis=-1)
        tipo = np.concatenate([tipo] + extra_k, axis=-1)
        deltas = np.stack([np.asarray(dl, np.int16) for _, dl in cambios], axis=1)
    orden = np.argsort(t, axis=-1, kind="stable")
    t = np.take_along_axis(t, orden, -1)
    tipo = np.take_along_axis(tipo, orden, -1)
    return {"t": np.ascontiguousarray(t.transpose(2, 0, 1)),
            "tipo": np.ascontiguousarray(tipo.transpose(2, 0, 1)),
            "deltas": deltas, "G": G}


# =====================================================================
# Función 2: la estación evento por evento (vectorizado en estaciones x estados x réplicas)
# =====================================================================
def simular(ev, B0, C, renta=None, recibe=None, minutos=False, solo_demanda=False):
    """
    ev: salida de generar_eventos. B0: (I,) , (I, S) o (I, S, R) estados iniciales; C: (I,).
    Reglas: retiro con B > 0 (y renta) -> B-1, si no se pierde; devolución con B < C
    (y recibe) -> B+1, si no se rechaza.
    Registra, por (i, s, r): si alguna lectura de minuto 1..60 mostró B = 0 o B = C
    (vac_min, lle_min), si lo tocó en cualquier instante (vac_cont, lle_cont), minutos
    vacía y llena, retiros perdidos, devoluciones rechazadas y B final.
    minutos=True (sólo con S = 1): estado en cada minuto 1..60 -> st_min (I, R, 60).
    """
    t_all, tipo_all, deltas = ev["t"], ev["tipo"], ev["deltas"]
    N, I, R = t_all.shape
    B0 = np.asarray(B0)
    if B0.ndim == 1:
        B0 = B0[:, None]
    if B0.ndim == 2:
        B = np.repeat(B0[:, :, None], R, axis=2).astype(np.int16)
    else:
        B = B0.astype(np.int16).copy()
    S = B.shape[1]
    Cb = np.asarray(C, np.int16)[:, None, None]
    rb = np.ones((I, 1, 1), bool) if renta is None else np.asarray(renta, bool)[:, None, None]
    db = np.ones((I, 1, 1), bool) if recibe is None else np.asarray(recibe, bool)[:, None, None]
    B_ini = B.copy()
    perdidos = np.zeros((I, S, R), np.int16)
    rechazados = np.zeros((I, S, R), np.int16)
    if not solo_demanda:
        vac_min = np.zeros((I, S, R), bool)
        lle_min = np.zeros((I, S, R), bool)
        vac_cont = np.zeros((I, S, R), bool)
        lle_cont = np.zeros((I, S, R), bool)
        min_vac = np.zeros((I, S, R), np.float32)
        min_lle = np.zeros((I, S, R), np.float32)
    hist = np.empty((N, I, R), np.int16) if minutos else None
    prev = np.zeros((I, 1, R), np.float32)

    def tramo(prev, t_eff):
        # el estado B se mantiene en [prev, t_eff): ¿hay una lectura de minuto adentro?
        dur = np.maximum(t_eff - prev, 0)
        m0 = np.maximum(np.ceil(prev), 1)
        visible = (m0 < t_eff) & (m0 <= H)
        vacia = B == 0
        llena = B == Cb
        np.logical_or(vac_min, visible & vacia, out=vac_min)
        np.logical_or(lle_min, visible & llena, out=lle_min)
        np.logical_or(vac_cont, (dur > 0) & vacia, out=vac_cont)
        np.logical_or(lle_cont, (dur > 0) & llena, out=lle_cont)
        min_vac[...] += dur * vacia
        min_lle[...] += dur * llena

    for j in range(N):
        t = t_all[j][:, None, :]
        tp = tipo_all[j][:, None, :]
        t_eff = np.minimum(t, FIN)
        if not solo_demanda:
            tramo(prev, t_eff)
        es_r = tp == -1
        es_d = tp == 1
        sirve_r = es_r & (B > 0) & rb
        sirve_d = es_d & (B < Cb) & db
        perdidos += es_r & ~sirve_r
        rechazados += es_d & ~sirve_d
        B += sirve_d.astype(np.int16) - sirve_r.astype(np.int16)
        if deltas is not None:
            for k in range(deltas.shape[1]):
                m = tp == 10 + k
                if m.any():
                    B = np.where(m, np.clip(B + deltas[:, k][:, None, None], 0, Cb), B).astype(np.int16)
        if minutos:
            hist[j] = B[:, 0, :]
        prev = t_eff
    if not solo_demanda:
        tramo(prev, np.full_like(prev, FIN))

    out = {"perdidos": perdidos, "rechazados": rechazados, "B_fin": B}
    if not solo_demanda:
        out.update(vac_min=vac_min, lle_min=lle_min, vac_cont=vac_cont, lle_cont=lle_cont,
                   min_vac=min_vac, min_lle=min_lle)
    if minutos:
        st = np.empty((I, R, H), np.int16)
        tt = t_all.transpose(1, 2, 0)                                   # (I, R, N)
        hh = hist.transpose(1, 2, 0)
        for m in range(1, H + 1):
            k = (tt <= m).sum(-1)
            val = np.take_along_axis(hh, np.maximum(k - 1, 0)[..., None], -1)[..., 0]
            st[:, :, m - 1] = np.where(k == 0, B_ini[:, 0, :], val)
        out["st_min"] = st
    return out


# =====================================================================
# Función 3b: probabilidad exacta con la cadena de Markov
# =====================================================================
def prob_exacta(lam, mu, B0, C, objetivo="vacia", renta=True, recibe=True):
    """
    P(la estación toca 0 (o C) antes de 60 min), tasas constantes por bloque de 15 min.
    El estado objetivo es absorbente; el otro extremo es reflejante.
    """
    from scipy.linalg import expm
    B0, C = int(B0), int(C)
    if C <= 0:
        return np.nan
    n = C + 1
    v = np.zeros(n)
    v[min(max(B0, 0), C)] = 1.0
    absorb = 0 if objetivo == "vacia" else C
    for k in range(len(lam)):
        l = lam[k] if renta else 0.0
        u = mu[k] if recibe else 0.0
        Q = np.diag(np.full(n - 1, u), 1) + np.diag(np.full(n - 1, l), -1)
        Q[absorb, :] = 0.0
        Q -= np.diag(Q.sum(1))
        v = v @ expm(Q * 0.25)                                         # 15 min = 0.25 h
    return float(v[absorb])


# =====================================================================
# Función 4: planes del camión
# =====================================================================
def plan_voraz(G, B0, C, ok, Q=cfg.Q_CAMION, max_tr=cfg.MAX_TRASLADOS, mejora_min=cfg.MEJORA_MIN):
    """
    G[i, s]: demanda no atendida esperada de la estación i si parte con s bicis.
    Elige hasta max_tr traslados (o, d, q), cada vez el de mayor mejora.
    """
    I, S = G.shape
    delta = np.zeros(I, int)
    rol = np.zeros(I, int)          # +1 ya fue origen, -1 ya fue destino
    plan = []
    for _ in range(max_tr):
        s = B0 + delta
        mejor = (-np.inf, None)
        for q in range(1, Q + 1):
            so, sd = s - q, s + q
            g_sal = np.full(I, -np.inf)
            okq = ok & (so >= 0) & (rol >= 0)
            g_sal[okq] = G[okq, s[okq]] - G[okq, so[okq]]
            g_ent = np.full(I, -np.inf)
            okd = ok & (sd <= C) & (sd < S) & (rol <= 0)
            g_ent[okd] = G[okd, s[okd]] - G[okd, sd[okd]]
            M = g_sal[:, None] + g_ent[None, :]
            np.fill_diagonal(M, -np.inf)
            k = np.argmax(M)
            if M.flat[k] > mejor[0]:
                mejor = (M.flat[k], (k // I, k % I, q))
        if mejor[1] is None or not np.isfinite(mejor[0]) or mejor[0] < mejora_min:
            break
        o, d, q = mejor[1]
        delta[o] -= q
        delta[d] += q
        rol[o], rol[d] = 1, -1
        plan.append((int(o), int(d), int(q), float(mejor[0])))
    return plan


def plan_umbral(B0, C, ok, Q=cfg.Q_CAMION, max_tr=cfg.MAX_TRASLADOS):
    """Regla de referencia: de > 80 % a < 20 %, dejando ambas cerca del 50 %."""
    occ = np.where(ok, B0 / np.maximum(C, 1), np.nan)
    orig = [i for i in np.argsort(-np.nan_to_num(occ, nan=-1)) if ok[i] and occ[i] > cfg.UMBRAL_ALTO]
    dest = [i for i in np.argsort(np.nan_to_num(occ, nan=9)) if ok[i] and occ[i] < cfg.UMBRAL_BAJO]
    plan = []
    for o, d in zip(orig, dest):
        if len(plan) >= max_tr:
            break
        q = min(B0[o] - int(np.ceil(cfg.OCUPACION_OBJETIVO * C[o])),
                int(np.floor(cfg.OCUPACION_OBJETIVO * C[d])) - B0[d], Q)
        if q > 0:
            plan.append((int(o), int(d), int(q), np.nan))
    return plan


def delta_de(plan, I):
    d = np.zeros(I, int)
    for o, de, q, _ in plan:
        d[o] -= q
        d[de] += q
    return d


def km(lat1, lon1, lat2, lon2):
    p = np.radians
    a = (np.sin(p(lat2 - lat1) / 2) ** 2
         + np.cos(p(lat1)) * np.cos(p(lat2)) * np.sin(p(lon2 - lon1) / 2) ** 2)
    return 2 * 6371 * np.arcsin(np.sqrt(a))


def tiempos_plan(plan, lat, lon):
    """Minuto de carga y de descarga de cada traslado si el camión parte en el primer origen."""
    t, pos, out = 0.0, None, []
    vel = cfg.VEL_KMH / 60.0
    for o, d, q, _ in plan:
        if pos is not None:
            t += km(lat[pos], lon[pos], lat[o], lon[o]) * cfg.FACTOR_RUTA / vel
        t += cfg.MIN_CARGA
        carga = t
        t += km(lat[o], lon[o], lat[d], lon[d]) * cfg.FACTOR_RUTA / vel + cfg.MIN_DESCARGA
        out.append((carga, t))
        pos = d
    return out


def resumen_pareado(x):
    """Media e intervalo de 95 % (t) de una muestra de réplicas."""
    x = np.asarray(x, float)
    m = x.mean()
    se = x.std(ddof=1) / np.sqrt(len(x)) if len(x) > 1 else np.nan
    return m, m - 1.96 * se, m + 1.96 * se


# =====================================================================
# El gemelo
# =====================================================================
class Gemelo:
    def __init__(self, fecha_ref=None, en_vivo=False, usar_parametros_ajuste=True, feed_desde=None):
        self.est = leer_estaciones()
        self.I = len(self.est)
        self.lat = self.est["lat"].astype(float).values if "lat" in self.est else np.zeros(self.I)
        self.lon = self.est["lon"].astype(float).values if "lon" in self.est else np.zeros(self.I)
        self.kappa = self.est["kappa"].astype(float).values
        self.en_vivo = en_vivo
        self.feed_desde = feed_desde
        extra = pronostico_clima_en_vivo() if en_vivo else None
        self.clima = leer_clima(extra)
        self.fclima = factores_por_hora(self.clima, tabla_factores_clima())
        self.panel = Panel(leer_feed(self.est, desde=feed_desde), self.est)
        print(self.panel.resumen())
        ref = pd.Timestamp(fecha_ref) if fecha_ref is not None else self.panel.fechas[0]
        if buscar_viajes():
            ev, sistema = leer_viajes(self.est)
            dias = dias_historia(sistema, ref)
            self.lam_base_ret, self.lam_base_dev, self.tabla_base = perfil_base(ev, dias, self.est, self.clima)
            self.dias_historia = dias
        elif os.path.isfile(cfg.ARCHIVO_PERFIL_BASE):
            self.lam_base_ret, self.lam_base_dev, self.tabla_base = leer_perfil_guardado(self.est)
            self.dias_historia = None
        else:
            raise SystemExit(f"No hay archivos de viajes ({', '.join(cfg.VIAJES)}) ni perfil base guardado "
                             f"({cfg.ARCHIVO_PERFIL_BASE}). Corre 'preparar' en una carpeta con los viajes.")
        self.params = {"W": cfg.W_DIAS, "m": cfg.M_CONFIANZA, "usar_phi": cfg.USAR_PHI}
        if usar_parametros_ajuste and os.path.isfile(cfg.ARCHIVO_PARAMETROS):
            with open(cfg.ARCHIVO_PARAMETROS, encoding="utf-8") as fh:
                p = json.load(fh)
            self.params.update({k: p[k] for k in ("W", "m", "usar_phi") if k in p})
            print(f"Parámetros del ajuste: W = {self.params['W']}, m = {self.params['m']}, "
                  f"phi = {'sí' if self.params['usar_phi'] else 'no'}")

    def actualizar(self):
        """Vuelve a leer el feed (sólo archivos nuevos) y, en vivo, el pronóstico del clima."""
        if self.en_vivo:
            self.clima = leer_clima(pronostico_clima_en_vivo())
            self.fclima = factores_por_hora(self.clima, tabla_factores_clima())
        self.panel = Panel(leer_feed(self.est, desde=self.feed_desde), self.est)

    # ---------------- clima ----------------
    def fc(self, hora, tipo, evento):
        col = f"f_{evento}_{tipo}"
        if col not in self.fclima:
            return 1.0
        v = self.fclima[col].get(pd.Timestamp(hora).floor("h"), 1.0)
        return 1.0 if not np.isfinite(v) else float(v)

    def phi(self, t0, usar_phi=None):
        usar = self.params["usar_phi"] if usar_phi is None else usar_phi
        if not usar:
            return 0.0
        h = pd.Timestamp(t0).hour
        for (a, b), v in cfg.PHI_POR_FRANJA.items():
            if a <= h < b:
                return v
        return 0.0

    def rng(self, t0, uso):
        return np.random.default_rng([cfg.SEMILLA, int(pd.Timestamp(t0).value // 60_000_000_000), uso])

    # ---------------- Función 1: tasas ----------------
    def _mezcla(self, win, fecha, b, m):
        """Pasos 1.1 a 1.3 para el bloque b de `fecha`: perfil base, ventana corregida, mezcla."""
        t = tipo_idx(fecha)
        base_r = self.lam_base_ret[t, :, b]
        base_d = self.lam_base_dev[t, :, b]
        z = np.zeros(self.I)
        if t == 1 or not win:
            return base_r, base_d, z, z, base_r * np.nan, base_d * np.nan
        P = self.panel
        h = b // 4
        res = []
        for nb, ne, base, ev in [(P.bret, P.bexr, base_r, "ret"), (P.bdev, P.bexd, base_d, "dev")]:
            f = np.array([self.fc(P.fechas[k] + pd.Timedelta(hours=h), 0, ev) for k in win])
            n = nb[:, win, b].astype(float)
            mins = ne[:, win, b].astype(float).sum(1)
            n_def = (n / f[None, :]).sum(1)
            with np.errstate(invalid="ignore", divide="ignore"):
                vent = np.where(mins > 0, self.kappa * 60 * n_def / mins, np.nan)
            # n efectivo: eventos vistos o, si no se vio ninguno, los que el perfil base esperaba
            # en esos minutos (así una ventana sin eventos también informa)
            n_ef = np.maximum(n.sum(1), base * mins / 60)
            w = np.where(mins > 0, n_ef / (n_ef + m), 0.0)
            mez = w * np.nan_to_num(vent) + (1 - w) * base
            res.append((mez, w, vent))
        (mr, wr, vr), (md, wd, vd) = res
        return mr, md, wr, wd, vr, vd

    def factor_dia(self, t0, win, m):
        """Paso 1.4: factor común (O + a) / (E + a) de la última hora, retiros y devoluciones."""
        P = self.panel
        fin = pd.Timestamp(t0).floor("15min")
        O = {"ret": 0.0, "dev": 0.0}
        E = {"ret": 0.0, "dev": 0.0}
        for j in range(1, 5):
            s = fin - pd.Timedelta(minutes=15 * j)
            d = P.dia(s)
            if s.hour not in cfg.HORAS_SERVICIO or not (0 <= d < P.n_dias):
                continue
            b = bloque_de(s)
            mr, md, *_ = self._mezcla(win, s.normalize(), b, m)
            t = tipo_idx(s)
            O["ret"] += float((self.kappa * P.bret[:, d, b]).sum())
            O["dev"] += float((self.kappa * P.bdev[:, d, b]).sum())
            E["ret"] += float((mr * self.fc(s, t, "ret") * P.bexr[:, d, b] / 60).sum())
            E["dev"] += float((md * self.fc(s, t, "dev") * P.bexd[:, d, b] / 60).sum())
        a = cfg.A_FACTOR
        F = {e: float(np.clip((O[e] + a) / (E[e] + a), cfg.F_MIN, cfg.F_MAX)) for e in O}
        return F, O, E

    def tasas(self, t0, W=None, m=None, usar_ventana=True, usar_F=True, usar_clima=True):
        """lam, mu (I, 4) en eventos/hora para los 4 bloques de 15 min desde t0, y su detalle."""
        W = self.params["W"] if W is None else W
        m = self.params["m"] if m is None else m
        t0 = pd.Timestamp(t0)
        win = self.panel.dias_ventana(t0, W) if usar_ventana else []
        lam = np.zeros((self.I, K_BLOQUES))
        mu = np.zeros((self.I, K_BLOQUES))
        det = []
        for k in range(K_BLOQUES):
            s = t0 + pd.Timedelta(minutes=15 * k)
            b = bloque_de(s)
            mr, md, wr, wd, vr, vd = self._mezcla(win, s.normalize(), b, m)
            t = tipo_idx(s)
            cr = self.fc(s, t, "ret") if usar_clima else 1.0
            cd = self.fc(s, t, "dev") if usar_clima else 1.0
            lam[:, k] = mr * cr
            mu[:, k] = md * cd
            det.append(pd.DataFrame({"code": self.est["code"], "bloque": f"{s:%H:%M}",
                                     "base_ret": self.lam_base_ret[t, :, b], "vent_ret": vr, "w_ret": wr,
                                     "base_dev": self.lam_base_dev[t, :, b], "vent_dev": vd, "w_dev": wd,
                                     "clima_ret": cr, "clima_dev": cd}))
        F, O, E = self.factor_dia(t0, win, m) if usar_F else ({"ret": 1.0, "dev": 1.0}, {}, {})
        lam *= F["ret"]
        mu *= F["dev"]
        det = pd.concat(det, ignore_index=True)
        det["F_ret"], det["F_dev"] = F["ret"], F["dev"]
        info = {"F": F, "O": O, "E": E, "dias_ventana": [f"{self.panel.fechas[k]:%Y-%m-%d}" for k in win]}
        return lam, mu, det, info

    # ---------------- estado y lo observado ----------------
    def estado(self, t0):
        P = self.panel
        p = P.pos(t0)
        if not (0 <= p < P.T):
            raise ValueError(f"{t0} está fuera del periodo con lecturas del feed")
        B, D = P.B[:, p], P.D[:, p]
        ok = P.dato[:, p] & np.isfinite(B) & np.isfinite(D) & ((np.nan_to_num(B) + np.nan_to_num(D)) > 0)
        B0 = np.where(ok, np.nan_to_num(B), 0).astype(int)
        C = np.where(ok, np.nan_to_num(B) + np.nan_to_num(D), 1).astype(int)
        return {"B0": B0, "C": C, "ok": ok, "renta": P.renta[:, p], "recibe": P.recibe[:, p]}

    def estado_vivo(self):
        try:
            ahora, st = estado_en_vivo(self.est)
        except Exception as ex:
            t = self.panel.ultima_lectura()
            print(f"Aviso: no pude leer el feed en vivo ({ex}); uso la última lectura guardada ({t:%d/%m %H:%M})")
            return t, self.estado(t)
        B = pd.to_numeric(st["num_bikes_available"], errors="coerce").values
        D = pd.to_numeric(st["num_docks_available"], errors="coerce").values
        ok = np.isfinite(B) & np.isfinite(D) & (np.nan_to_num(B) + np.nan_to_num(D) > 0)
        renta = pd.to_numeric(st.get("is_renting", 1), errors="coerce").fillna(1).values != 0
        recibe = pd.to_numeric(st.get("is_returning", 1), errors="coerce").fillna(1).values != 0
        return ahora, {"B0": np.where(ok, np.nan_to_num(B), 0).astype(int),
                       "C": np.where(ok, np.nan_to_num(B) + np.nan_to_num(D), 1).astype(int),
                       "ok": ok, "renta": renta, "recibe": recibe}

    def observado(self, t0):
        """Lo que ocurrió en (t0, t0+60]: vacía, llena, B final, camiones, cobertura."""
        P = self.panel
        p = P.pos(t0)
        if p + H >= P.T or p < 0:
            return None
        sl = slice(p + 1, p + H + 1)
        B = P.B[:, sl]
        C = B + P.D[:, sl]
        dato = P.dato[:, sl]
        cov = dato.sum(1)
        return {"y_vac": ((B == 0) & dato).any(1), "y_lle": ((B == C) & dato).any(1),
                "B60": P.B[:, p + H], "camion": (P.camion[:, sl] != 0).any(1),
                "ok": cov >= cfg.MIN_COBERTURA_HORA, "trayectoria": B}

    # ---------------- Función 3: pronóstico ----------------
    def pronosticar(self, t0, R=None, W=None, m=None, usar_phi=None, estado=None, minutos=False,
                    usar_ventana=True, usar_F=True, uso=0):
        R = cfg.R if R is None else R
        t0 = pd.Timestamp(t0)
        lam, mu, det, info = self.tasas(t0, W, m, usar_ventana=usar_ventana, usar_F=usar_F)
        e = self.estado(t0) if estado is None else estado
        phi = self.phi(t0, usar_phi)
        ev = generar_eventos(lam, mu, R, self.rng(t0, uso), phi)
        out = simular(ev, e["B0"], e["C"], e["renta"], e["recibe"], minutos=minutos)
        ok = e["ok"]

        def media(a):
            x = a[:, 0, :].mean(-1).astype(float)
            return np.where(ok, x, np.nan)

        Bf = out["B_fin"][:, 0, :].astype(float)
        q = np.percentile(Bf, [5, 10, 50, 90, 95], axis=1)
        res = {"t0": t0, "lam": lam, "mu": mu, "detalle": det, "info": info, "phi": phi, "estado": e,
               "p_vac": media(out["vac_min"]), "p_lle": media(out["lle_min"]),
               "p_vac_cont": media(out["vac_cont"]), "p_lle_cont": media(out["lle_cont"]),
               "min_vac": media(out["min_vac"]), "min_lle": media(out["min_lle"]),
               "perdidos": media(out["perdidos"]), "rechazados": media(out["rechazados"]),
               "q05": q[0], "q10": q[1], "q50": q[2], "q90": q[3], "q95": q[4], "R": R}
        for k in ("q05", "q10", "q50", "q90", "q95"):
            res[k] = np.where(ok, res[k], np.nan)
        if minutos:
            res["st_min"] = out["st_min"]
        return res

    def exactas(self, pron):
        """Probabilidad exacta (cadena de Markov, sin phi) para cada estación del pronóstico."""
        e = pron["estado"]
        pv, pl = np.full(self.I, np.nan), np.full(self.I, np.nan)
        for i in range(self.I):
            if e["ok"][i]:
                pv[i] = prob_exacta(pron["lam"][i], pron["mu"][i], e["B0"][i], e["C"][i], "vacia",
                                    e["renta"][i], e["recibe"][i])
                pl[i] = prob_exacta(pron["lam"][i], pron["mu"][i], e["B0"][i], e["C"][i], "llena",
                                    e["renta"][i], e["recibe"][i])
        return pv, pl

    # ---------------- Función 4: planes ----------------
    def planificar(self, pron, R=None, tiempos=True):
        R = cfg.R_PLANES if R is None else R
        t0, e = pron["t0"], pron["estado"]
        lam, mu, phi = pron["lam"], pron["mu"], pron["phi"]
        B0, C, ok = e["B0"], e["C"], e["ok"]
        # g_i(s): demanda no atendida esperada partiendo con s bicis (mismas réplicas para todo s)
        S = int(C[ok].max()) + 1 if ok.any() else 1
        Bs = np.minimum(np.arange(S)[None, :], C[:, None])
        ev = generar_eventos(lam, mu, R, self.rng(t0, 1), phi)
        out = simular(ev, Bs, C, e["renta"], e["recibe"], solo_demanda=True)
        U = (out["perdidos"].astype(np.float32) + out["rechazados"]).mean(-1)
        G = np.where(np.arange(S)[None, :] <= C[:, None], U, np.inf)
        planes = {"Sin acción": [], "Regla umbral": plan_umbral(B0, C, ok),
                  "Gemelo (voraz)": plan_voraz(G, B0, C, ok)}

        # Evaluación con réplicas NUEVAS (no las usadas para elegir) y comunes a los tres planes
        nombres = list(planes)
        Bm = np.stack([np.clip(B0 + delta_de(planes[n], self.I), 0, C) for n in nombres], axis=1)
        sem = self.rng(t0, 2)
        ev2 = generar_eventos(lam, mu, R, sem, phi)
        out2 = simular(ev2, Bm, C, e["renta"], e["recibe"], solo_demanda=True)
        Ua = (out2["perdidos"].astype(float) + out2["rechazados"]) * ok[:, None, None]
        D = Ua.sum(0)                                                    # (planes, R)
        filas = []
        for k, n in enumerate(nombres):
            mm, lo, hi = resumen_pareado(D[k])
            dm, dlo, dhi = resumen_pareado(D[0] - D[k])
            filas.append({"plan": n, "traslados": len(planes[n]), "bicis_movidas": sum(p[2] for p in planes[n]),
                          "no_atendida_media": mm, "ic95_inf": lo, "ic95_sup": hi,
                          "atendidos_extra_vs_sin_accion": dm, "dif_ic95_inf": dlo, "dif_ic95_sup": dhi})
        # Sensibilidad: el plan del gemelo con tiempos de viaje del camión
        if tiempos and planes["Gemelo (voraz)"]:
            cambios = []
            for (o, d, q, _), (tc, td) in zip(planes["Gemelo (voraz)"], tiempos_plan(planes["Gemelo (voraz)"],
                                                                                       self.lat, self.lon)):
                if tc < H:
                    dl = np.zeros(self.I, int)
                    dl[o] = -q
                    cambios.append((tc, dl))
                if td < H:
                    dl = np.zeros(self.I, int)
                    dl[d] = q
                    cambios.append((td, dl))
            ev3 = generar_eventos(lam, mu, R, self.rng(t0, 2), phi, cambios=cambios)
            out3 = simular(ev3, B0, C, e["renta"], e["recibe"], solo_demanda=True)
            D3 = ((out3["perdidos"].astype(float) + out3["rechazados"]) * ok[:, None, None]).sum(0)[0]
            mm, lo, hi = resumen_pareado(D3)
            dm, dlo, dhi = resumen_pareado(D[0] - D3)
            filas.append({"plan": "Gemelo (voraz) con tiempos de viaje", "traslados": len(planes["Gemelo (voraz)"]),
                          "bicis_movidas": sum(p[2] for p in planes["Gemelo (voraz)"]),
                          "no_atendida_media": mm, "ic95_inf": lo, "ic95_sup": hi,
                          "atendidos_extra_vs_sin_accion": dm, "dif_ic95_inf": dlo, "dif_ic95_sup": dhi})
        comp = pd.DataFrame(filas)
        lista = []
        for n in nombres[1:]:
            tt = tiempos_plan(planes[n], self.lat, self.lon) if planes[n] else []
            for k, (o, d, q, mej) in enumerate(planes[n]):
                lista.append({"plan": n, "orden": k + 1, "origen": self.est["code"][o],
                              "origen_nombre": self.est["nombre_corto"][o], "destino": self.est["code"][d],
                              "destino_nombre": self.est["nombre_corto"][d], "bicis": q,
                              "B_origen": B0[o], "C_origen": C[o], "B_destino": B0[d], "C_destino": C[d],
                              "mejora_esperada": mej, "min_carga": tt[k][0], "min_descarga": tt[k][1]})
        return {"planes": planes, "comparacion": comp, "traslados": pd.DataFrame(lista), "G": G}

    # ---------------- Referencia: sin resincronizar ----------------
    def sin_resincronizar_dia(self, fecha, R=None, usar_phi=None):
        """
        Mismo modelo calibrado una sola vez: estado de las 06:00, perfil base (con clima),
        sin ventana ni factor del día, simulado hora a hora hasta las 24:00.
        Devuelve los estados por minuto (I, R, 1080) desde las 06:01.
        """
        R = cfg.R if R is None else R
        fecha = pd.Timestamp(fecha).normalize()
        t_ini = fecha + pd.Timedelta(hours=6)
        e = self.estado(t_ini)
        t = tipo_idx(fecha)
        rng = self.rng(t_ini, 3)
        horas = list(range(6, 24))
        st = np.empty((self.I, R, 60 * len(horas)), np.int16)
        B = np.repeat(e["B0"][:, None, None], R, axis=2)
        for k, h in enumerate(horas):
            bl = [h * 4 + j for j in range(4)]
            hora = fecha + pd.Timedelta(hours=h)
            lam = self.lam_base_ret[t][:, bl] * self.fc(hora, t, "ret")
            mu = self.lam_base_dev[t][:, bl] * self.fc(hora, t, "dev")
            ev = generar_eventos(lam, mu, R, rng, self.phi(hora, usar_phi))
            out = simular(ev, B, e["C"], minutos=True)
            st[:, :, 60 * k:60 * (k + 1)] = out["st_min"]
            B = out["B_fin"]
        return {"inicio": t_ini, "st": st, "C": e["C"], "ok": e["ok"]}

    @staticmethod
    def pron_sin_resinc(sr, t0):
        a = int((pd.Timestamp(t0) - sr["inicio"]) / pd.Timedelta(minutes=1))
        st = sr["st"][:, :, a:a + H]
        C = sr["C"][:, None, None]
        pv = (st == 0).any(-1).mean(-1)
        pl = (st == C).any(-1).mean(-1)
        q = np.percentile(st[:, :, -1].astype(float), [10, 50, 90], axis=1)
        ok = sr["ok"]
        return {"p_vac": np.where(ok, pv, np.nan), "p_lle": np.where(ok, pl, np.nan),
                "q10": np.where(ok, q[0], np.nan), "q50": np.where(ok, q[1], np.nan),
                "q90": np.where(ok, q[2], np.nan)}


# =====================================================================
# Persistencia probabilística
# =====================================================================
def grupo_persistencia(x):
    return np.digitize(np.nan_to_num(x, nan=-1), cfg.CORTES_PERSISTENCIA)


def tabla_persistencia(B0, D0, y_vac, y_lle):
    """Frecuencia de quedar vacía (llena) en la hora siguiente según las bicis (anclajes) de ahora."""
    gv, gl = grupo_persistencia(B0), grupo_persistencia(D0)
    n = len(cfg.CORTES_PERSISTENCIA) + 1
    fv = [np.mean(y_vac[gv == g]) if (gv == g).any() else np.nan for g in range(n)]
    fl = [np.mean(y_lle[gl == g]) if (gl == g).any() else np.nan for g in range(n)]
    etiquetas = ["0"] + [f"{a}" if b - a == 1 else f"{a}-{b - 1}"
                         for a, b in zip(cfg.CORTES_PERSISTENCIA[:-1], cfg.CORTES_PERSISTENCIA[1:])] \
        + [f"{cfg.CORTES_PERSISTENCIA[-1]}+"]
    return pd.DataFrame({"grupo": range(n), "rango": etiquetas, "p_vacia": fv, "p_llena": fl,
                         "n_vac": [(gv == g).sum() for g in range(n)], "n_lle": [(gl == g).sum() for g in range(n)]})
