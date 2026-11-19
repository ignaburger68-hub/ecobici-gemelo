"""
tablero.py - Tablero del gemelo digital Ecobici (interfaz para la presentación)

Uso (desde la misma carpeta que gemelo.py):
    py -3.14 -m pip install streamlit
    py -3.14 -m streamlit run tablero.py

Pestaña "Pronóstico":
  - Reproducción: eliges un día y una hora ya recolectados; muestra el pronóstico de la hora
    siguiente, el plan del camión y lo que efectivamente ocurrió.
  - En vivo: lee el feed de Ecobici ahora y pronostica la próxima hora. Con "Actualizar sola"
    se repite cada 15 minutos (y, si se pide, antes hace git pull para traer las lecturas nuevas).
Pestaña "Rendimiento": resultados de "evaluar" y del registro en tiempo real (gemelo_vivo/).
Pestaña "Tasas": cómo cambian las tasas en el día y entre días, frente a lo observado (tasas_gemelo.py).
"""
import os
import subprocess

import numpy as np
import pandas as pd
import streamlit as st

import config_gemelo as cfg
from datos_gemelo import es_habil
from gemelo import DIAS, ahora_local, simulacion_una_hora
from modelo_gemelo import Gemelo
import tasas_gemelo as tz

st.set_page_config(page_title="Gemelo digital Ecobici", layout="wide")
CARPETA_EVAL = os.path.join(cfg.CARPETA_RESULTADOS, "evaluacion")


@st.cache_resource(show_spinner="Cargando datos (viajes, feed y clima)...")
def cargar(en_vivo):
    return Gemelo(en_vivo=en_vivo)


def recargar_datos():
    """git pull y volver a leer todo (sin reiniciar el tablero)."""
    try:
        r = subprocess.run(["git", "pull"], capture_output=True, text=True, timeout=180)
        salida = (r.stdout + r.stderr).strip().splitlines()
        msg = salida[-1] if salida else "listo"
        st.session_state["aviso_recarga"] = ("ok" if r.returncode == 0 else "error", f"git pull: {msg}")
    except Exception as e:
        st.session_state["aviso_recarga"] = ("error", f"No se pudo hacer git pull ({e}); se releen los datos locales")
    st.cache_resource.clear()
    st.cache_data.clear()
    for k in ("pasado", "vivo"):
        st.session_state.pop(k, None)


def dias_y_horas(gem):
    """
    Días para Reproducción: hábiles con buena cobertura y, además, el día de hoy si tiene lecturas
    (aunque todavía no llegue al 50 % del día completo).
    """
    ultima = gem.panel.ultima_lectura()
    dias = [d for d in gem.panel.fechas if es_habil([d])[0] and gem.panel.cobertura_dia[d] >= cfg.MIN_COBERTURA_DIA]
    hoy = ahora_local().normalize()
    if ultima is not None and ultima.normalize() == hoy and es_habil([hoy])[0] and hoy not in dias:
        dias.append(hoy)
    return dias, ultima


@st.cache_data(show_spinner="Calculando las tasas del día...")
def tasas_dia(dia, evento, estacion):
    return tz.serie_dia(cargar(False), dia, evento, estacion)


@st.cache_data(show_spinner="Calculando la misma hora en cada día...")
def tasas_hora(hora, evento, estacion):
    return tz.serie_hora(cargar(False), hora, evento, estacion)


@st.cache_data(show_spinner="Calculando el mapa de calor (puede tardar unos segundos)...")
def tasas_mapa(evento, estacion):
    return tz.mapa_calor(cargar(False), evento, estacion)


def pestana_tasas():
    gt = cargar(False)
    st.markdown("Cómo cambian las tasas que usa el gemelo (viajes por hora que espera en cada estación) "
                "**durante el día** y **entre días**, frente a lo que realmente ocurrió. Cada tasa se calcula "
                "como la habría calculado el gemelo en ese momento, sólo con la información hasta ese instante.")
    c1, c2, c3, c4 = st.columns([1, 1.4, 1.2, 0.8])
    evento = {"Retiros": "ret", "Devoluciones": "dev"}[c1.radio("Evento", ["Retiros", "Devoluciones"],
                                                                 horizontal=True, key="tz_ev")]
    opciones = ["todas"] + list(gt.est["code"])
    nombres = dict(zip(gt.est["code"], gt.est["nombre_corto"]))
    estacion = c2.selectbox("Estaciones", opciones, key="tz_est",
                            format_func=lambda c: "Las 30 estaciones (sumadas)" if c == "todas"
                            else f"{c} {str(nombres.get(c, ''))[:28]}")
    dias = tz.dias_disponibles(gt)
    hoy = ahora_local().normalize()
    dia = c3.selectbox("Día (vista 1)", dias[::-1], key="tz_dia",
                       format_func=lambda d: tz._etiqueta_dia(d) + (" · hoy" if d == hoy else ""))
    horas = [f"{h:02d}:00" for h in range(6, 23)]
    hora = c4.selectbox("Hora (vista 2)", horas, index=horas.index("08:00"), key="tz_hora")
    est = None if estacion == "todas" else estacion

    st.markdown("#### 1 · A lo largo del día")
    st.caption("Barras grises: viajes observados. Líneas: lo que esperaba el modelo, paso a paso. "
               "**Perfil base** (verde) es lo normal de largo plazo; **Base + ventana** (naranja) lo corrige con "
               "lo que pasó a esa hora en los últimos días hábiles; **Modelo** (azul) es la tasa final, que además "
               "multiplica por el clima y por el **factor del día**. Abajo se ve cómo cambian esos dos factores: "
               "si el factor del día sube de 1, en la última hora hubo más viajes de lo esperado y el modelo sube "
               "sus tasas. Con una sola estación se agrupa por hora, porque por bloque los conteos son muy pequeños.")
    s = tasas_dia(dia, evento, est)
    fig = tz.figura_dia(gt, s, evento, est)
    if fig is None:
        st.info("No hay lecturas para ese día.")
    else:
        st.pyplot(fig)

    st.markdown(f"#### 2 · La misma hora ({hora}) en distintos días")
    st.caption("Cada grupo es un día: barras = viajes observados en esa hora; líneas = lo esperado por el modelo, "
               "con las mismas tres etapas. Muestra cómo la **ventana** va aprendiendo de los días anteriores "
               "(la línea naranja se mueve, la verde no) y qué días fueron atípicos. Las barras claras son fines de "
               "semana o festivos, donde no se usa ventana.")
    s2 = tasas_hora(hora, evento, est)
    fig = tz.figura_hora(gt, s2, hora, evento, est)
    if fig is None:
        st.info("No hay datos para esa hora.")
    else:
        st.pyplot(fig)

    st.markdown("#### 3 · Mapa de calor: observado ÷ modelo")
    st.caption("Cada casilla es una hora de un día. **1** (blanco) = ocurrió lo que esperaba el modelo; "
               "**rojo** (> 1) = hubo más viajes de lo esperado; **azul** (< 1) = hubo menos. Sirve para ver de un "
               "vistazo en qué días u horas el modelo se queda corto o se pasa. Las casillas vacías son horas con "
               "menos de la mitad de los minutos con lecturas del feed.")
    m = tasas_mapa(evento, est)
    fig = tz.figura_mapa(gt, m, evento, est)
    if fig is None:
        st.info("Todavía no hay horas con datos suficientes.")
    else:
        st.pyplot(fig)
        r = m["razon"].dropna()
        st.caption(f"Mediana de observado ÷ modelo: **{r.median():.2f}** · la mitad de las horas entre "
                   f"{r.quantile(0.25):.2f} y {r.quantile(0.75):.2f} ({len(r)} horas con datos).")
    with st.expander("Descargar los datos de estas vistas"):
        st.download_button("Vista 1 (CSV)", tz._redondear(s).to_csv(index=False).encode("utf-8"),
                           f"tasas_dia_{dia:%Y-%m-%d}.csv", "text/csv")
        st.download_button("Vista 2 (CSV)", tz._redondear(s2).to_csv(index=False).encode("utf-8"),
                           f"tasas_hora_{hora.replace(':', '')}.csv", "text/csv")
        st.download_button("Mapa de calor (CSV)", tz._redondear(m).to_csv(index=False).encode("utf-8"),
                           "tasas_mapa_calor.csv", "text/csv")


def empaquetar(res):
    return {k: res[k] for k in ("t0", "tabla", "brier", "texto", "clima")} | {
        "traslados": res["plan"]["traslados"], "comparacion": res["plan"]["comparacion"],
        "fig_mapa": res["fig_mapa"], "fig_abanico": res["fig_abanico"], "info": res["pron"]["info"]}


@st.cache_resource(show_spinner="Simulando la próxima hora...", max_entries=20)
def correr_pasado(t0, R):
    return empaquetar(simulacion_una_hora(cargar(False), t0, R=R, guardar=False))


@st.cache_resource(show_spinner="Leyendo Ecobici y simulando la próxima hora...", max_entries=2)
def correr_vivo(tramo, R, pull):
    """`tramo` cambia cada 15 minutos: así el resultado se recalcula solo una vez por tramo."""
    gem = cargar(True)
    if pull:
        try:
            subprocess.run(["git", "pull", "-q"], timeout=120, check=False)
        except Exception:
            pass
    gem.actualizar()
    return empaquetar(simulacion_una_hora(gem, en_vivo=True, R=R, guardar=False))


def mostrar_clima(cl):
    """Clima de la hora simulada y cuánto cambia la demanda por él."""
    h = cl["hora"]
    st.markdown(f"**Clima {cl['fuente']} de {h:%H:%M} a {h + pd.Timedelta(hours=1):%H:%M} y su efecto en la "
                f"demanda** (día {cl['tipo_dia']})")
    if cl["fuente"] == "pronosticado":
        st.caption("Esta hora todavía no termina: el clima es el pronóstico meteorológico de Open-Meteo, "
                   "no lo registrado.")
    c1, c2, c3, c4, c5 = st.columns(5)
    if cl["hay_dato"]:
        dif = cl["temp_dif_c"]
        c1.metric("Temperatura", f"{cl['temperatura_c']:.1f} °C",
                  delta=f"{dif:+.1f} °C vs lo normal" if np.isfinite(dif) else None, delta_color="off")
        ll = cl["precipitacion_mm"]
        c2.metric("Lluvia", "sin dato" if not np.isfinite(ll) else
                  ("sin lluvia" if ll < cfg.UMBRAL_LLUVIA else f"{ll:.1f} mm/h"))
        c3.metric("Viento", f"{cl['viento_kmh']:.0f} km/h")
    else:
        c1.metric("Temperatura", "sin dato")
        c2.metric("Lluvia", "sin dato")
        c3.metric("Viento", "sin dato")
    c4.metric("Efecto en retiros", f"×{cl['efecto_ret']:.2f}", delta=f"{100 * (cl['efecto_ret'] - 1):+.0f} %",
              delta_color="off")
    c5.metric("Efecto en devoluciones", f"×{cl['efecto_dev']:.2f}", delta=f"{100 * (cl['efecto_dev'] - 1):+.0f} %",
              delta_color="off")
    if cl["factores"] is not None:
        with st.expander("¿De dónde sale el efecto del clima?"):
            st.caption("Cada condición tiene un factor (resultados_clima/factores_clima_gemelo.csv) y el modelo "
                       "multiplica los cuatro: ×1,00 = sin efecto; ×0,90 = 10 % menos viajes que con clima normal. "
                       "El efecto de arriba es el promedio de los 4 bloques de 15 minutos de la hora simulada.")
            st.dataframe(cl["factores"].rename(columns={
                "variable": "Variable", "categoria": "Condición", "factor_retiros": "Factor retiros",
                "factor_devoluciones": "Factor devoluciones"}).round(3), hide_index=True)
    elif not cl["hay_dato"]:
        st.caption("Sin datos de clima para esta hora: se toma como normal (factor 1). "
                   "Haz git pull para traer datos/clima/clima_horario.csv.")


def mostrar(r):
    tabla, t0 = r["tabla"], r["t0"]
    st.subheader(f"{DIAS[t0.dayofweek]} {t0:%d/%m/%Y %H:%M} → {t0 + pd.Timedelta(minutes=60):%H:%M}")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Estaciones con p(vacía) > 0,5", int((tabla["p_vacia"] > 0.5).sum()))
    c2.metric("Estaciones con p(llena) > 0,5", int((tabla["p_llena"] > 0.5).sum()))
    comp = r["comparacion"].set_index("plan")
    if "Gemelo (voraz)" in comp.index:
        c3.metric("Usuarios atendidos de más con el plan",
                  f"{comp.loc['Gemelo (voraz)', 'atendidos_extra_vs_sin_accion']:.1f}")
    c4.metric("Factor del día (retiros)", f"{r['info']['F']['ret']:.2f}")
    mostrar_clima(r["clima"])
    izq, der = st.columns([1.1, 1])
    with izq:
        st.pyplot(r["fig_mapa"])
    with der:
        comp = r["comparacion"]
        mejor = comp.loc[comp["mejor_regla"].astype(bool), "plan"].iloc[0] if "mejor_regla" in comp else None
        st.markdown("**Plan recomendado (gemelo) y la mejor regla umbral**")
        tr = r["traslados"]
        if len(tr):
            tr = tr[tr["plan"].isin(["Gemelo (voraz)", mejor])] if mejor else tr
            st.dataframe(tr[["plan", "orden", "origen", "destino", "bicis", "B_origen", "C_origen",
                             "B_destino", "C_destino", "mejora_esperada"]].round(2), hide_index=True)
        else:
            st.write("Ningún traslado mejora la hora lo suficiente.")
        st.markdown("**Demanda no atendida esperada (30 estaciones)**")
        st.caption("La **regla umbral** saca bicis de estaciones muy llenas (ocupación sobre el primer número) y las "
                   "lleva a estaciones muy vacías (bajo el segundo), dejando ambas cerca del 50 %. Se prueban 5 pares "
                   "de umbrales con las mismas réplicas simuladas; la que deja **menos demanda no atendida** en esta "
                   "hora aparece resaltada con ★ (si empatan, la que mueve menos bicis).")
        vista = comp[["plan", "no_atendida_media", "atendidos_extra_vs_sin_accion", "dif_ic95_inf", "dif_ic95_sup"]].copy()
        es_mejor = comp["mejor_regla"].astype(bool).values if "mejor_regla" in comp else np.zeros(len(comp), bool)
        vista["plan"] = [("★ " if m else "") + p for p, m in zip(vista["plan"], es_mejor)]
        vista = vista.rename(columns={"plan": "Plan", "no_atendida_media": "No atendida (media)",
                                      "atendidos_extra_vs_sin_accion": "Atendidos de más vs sin acción",
                                      "dif_ic95_inf": "IC95 inf", "dif_ic95_sup": "IC95 sup"})
        estilo = (vista.style
                  .apply(lambda f: ["background-color: rgba(46,139,87,0.28); font-weight: 700"
                                    if es_mejor[f.name] else "" for _ in f], axis=1)
                  .format("{:.1f}", subset=vista.columns[1:]))
        st.dataframe(estilo, hide_index=True)
        if r["brier"] is not None:
            st.markdown("**Lo que ocurrió: puntaje de Brier de esta hora** (menor es mejor; 0,25 = decir siempre 50 %)")
            st.dataframe(r["brier"].round(3), hide_index=True)
    st.pyplot(r["fig_abanico"])
    st.markdown("**Pronóstico por estación**")
    cols = ["code", "nombre", "perfil", "B_t0", "C", "retiros_h", "devoluciones_h", "p_vacia", "p_llena",
            "B_t60_mediana", "B_t60_ic80", "cambio_plan_gemelo"]
    cols += [c for c in ("vacia_real", "llena_real", "B_t60_real", "camion_operador") if c in tabla]
    st.dataframe(tabla[cols].sort_values("p_vacia", ascending=False), hide_index=True)
    with st.expander("Resumen en texto"):
        st.text(r["texto"])


st.title("Gemelo digital · 30 estaciones Ecobici")
with st.sidebar:
    modo = st.radio("Modo", ["Reproducción", "En vivo"])
    en_vivo = modo == "En vivo"
    gem = cargar(en_vivo)
    R = st.select_slider("Réplicas", [200, 500, 1000, 2000], value=cfg.R)
    t0 = None
    if en_vivo:
        auto = st.checkbox("Actualizar sola cada 15 minutos", value=True)
        pull = st.checkbox("Traer lecturas nuevas (git pull) antes de cada actualización", value=True,
                           help="Necesita que esta carpeta sea el repositorio del recolector")
    else:
        dias, ultima = dias_y_horas(gem)
        hoy = ahora_local().normalize()
        if not dias:
            st.warning("No hay días con lecturas suficientes. Usa «Recargar datos».")
            dias = [hoy]
        dia = st.selectbox("Día", dias[::-1], format_func=lambda d: f"{DIAS[d.dayofweek]} {d:%d/%m/%Y}"
                           + (" (hoy)" if d == hoy else ""))
        horas = pd.date_range(dia + pd.Timedelta(cfg.PRIMER_T0 + ":00"), dia + pd.Timedelta(cfg.ULTIMO_T0 + ":00"),
                              freq=f"{cfg.PASO_T0_MIN}min")
        if ultima is not None and ultima.normalize() == dia:
            horas = horas[horas <= ultima]          # hoy: sólo hasta la última lectura
        if len(horas) == 0:
            st.warning(f"Todavía no hay lecturas desde las {cfg.PRIMER_T0} de este día. "
                       "Usa «Recargar datos» más tarde.")
        else:
            completas = horas[horas + pd.Timedelta(minutes=60) <= ultima] if ultima is not None else horas
            defecto = completas[-1] if dia == hoy and len(completas) else (horas[7] if len(horas) > 7 else horas[0])
            t0 = st.select_slider("Hora (t0)", list(horas), value=defecto, format_func=lambda t: f"{t:%H:%M}")
            if ultima is not None and t0 + pd.Timedelta(minutes=60) > ultima:
                st.caption("Esta hora todavía no termina en los datos: se muestra el pronóstico, "
                           "pero aún no «lo que ocurrió».")
    ult = gem.panel.ultima_lectura()
    if ult is not None:
        st.caption(f"Última lectura cargada: {DIAS[ult.dayofweek]} {ult:%d/%m %H:%M}")
    if st.button("Recargar datos (git pull)", help="Trae las lecturas nuevas de GitHub y vuelve a leer todo, "
                 "sin reiniciar el tablero"):
        with st.spinner("Trayendo lecturas nuevas..."):
            recargar_datos()
        st.rerun()
    if "aviso_recarga" in st.session_state:
        tipo, msg = st.session_state.pop("aviso_recarga")
        (st.success if tipo == "ok" else st.warning)(msg)
    st.caption(f"W = {gem.params['W']} días · m = {gem.params['m']} · "
               f"phi {'sí' if gem.params['usar_phi'] else 'no'} · semilla {cfg.SEMILLA}")
    ejecutar = st.button("Simular la próxima hora", type="primary", disabled=(not en_vivo and t0 is None))

pest_pron, pest_rend, pest_tasas = st.tabs(["Pronóstico", "Rendimiento", "Tasas"])

with pest_pron:
    if en_vivo and auto:
        @st.fragment(run_every="60s")
        def vivo():
            ahora = ahora_local()
            tramo = ahora.floor("15min")
            r = correr_vivo(tramo, R, pull)
            prox = tramo + pd.Timedelta(minutes=15)
            st.caption(f"En vivo · se actualiza sola · próxima actualización a las {prox:%H:%M} "
                       f"(hora de Ciudad de México)")
            mostrar(r)
        vivo()
    elif en_vivo:
        if ejecutar:
            st.session_state["vivo"] = correr_vivo(ahora_local().floor("min"), R, pull)
        if "vivo" in st.session_state:
            mostrar(st.session_state["vivo"])
        else:
            st.info("Presiona «Simular la próxima hora» o activa «Actualizar sola».")
    else:
        if ejecutar:
            st.session_state["pasado"] = correr_pasado(t0, R)
        if "pasado" in st.session_state:
            mostrar(st.session_state["pasado"])
        else:
            st.info("Elige el día y la hora en el panel de la izquierda y presiona «Simular la próxima hora».")

with pest_rend:
    st.markdown("### Pronósticos hechos en tiempo real (registro automático)")
    a = os.path.join(cfg.CARPETA_VIVO, "resumen_vivo.csv")
    if os.path.isfile(a):
        tb = pd.read_csv(a)
        ev = os.path.join(cfg.CARPETA_VIVO, "evaluaciones.csv")
        if os.path.isfile(ev):
            t_ev = pd.to_datetime(pd.read_csv(ev, usecols=["t0"])["t0"]).drop_duplicates()
            st.info(f"Evalúa {len(t_ev)} pronósticos que hizo GitHub entre el {t_ev.min():%d/%m %H:%M} y el "
                    f"{t_ev.max():%d/%m %H:%M} (hora de Ciudad de México), cuya hora ya terminó. "
                    "El pronóstico que ves en la pestaña «Pronóstico» no está aquí: se evaluará una hora "
                    "después, cuando ya se sepa qué pasó. Haz «Recargar datos» para traer las evaluaciones nuevas.")
        st.caption("Cada pronóstico se hizo en el momento, sólo con la información de ese momento, "
                   "y se comparó con lo que ocurrió una hora después. Menor es mejor; 0,25 = decir siempre 50 %.")
        st.dataframe(tb.round(4), hide_index=True)
        img = os.path.join(cfg.CARPETA_VIVO, "brier_vivo.png")
        if os.path.isfile(img):
            st.image(img)
    else:
        st.info(f"Todavía no hay registro en vivo ({cfg.CARPETA_VIVO}/). Lo genera el comando 'ciclo' en GitHub; "
                "haz git pull para traerlo.")
    st.markdown("### Evaluación de la semana (comando evaluar)")
    a = os.path.join(CARPETA_EVAL, "resumen_evaluacion.txt")
    if os.path.isfile(a):
        with open(a, encoding="utf-8") as fh:
            st.text(fh.read())
        for nombre, titulo in [("brier_por_hora.png", "Puntaje de Brier por hora del día"),
                               ("calibracion.png", "Calibración"),
                               ("planes_por_hora.png", "Valor de los planes de rebalanceo (en simulación)")]:
            img = os.path.join(CARPETA_EVAL, nombre)
            if os.path.isfile(img):
                st.markdown(f"**{titulo}**")
                st.image(img)
    else:
        st.info("Todavía no hay evaluación. Se genera con: py -3.14 gemelo.py evaluar --desde ... --hasta ... --planes")

with pest_tasas:
    pestana_tasas()
