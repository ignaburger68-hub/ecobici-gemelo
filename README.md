# Gemelo digital Ecobici · 30 estaciones

Proyecto Simulación MIIIO/DIIIO 2-2026 · Tema 3: Gemelos digitales · Ignacio Chandia y Francisco Correa

Este repositorio hace dos cosas:

1. **Recolecta** cada minuto el estado de todas las estaciones de Ecobici (Ciudad de México) desde su feed público GBFS. Lo hace solo, en GitHub Actions, día y noche.
2. **Corre un gemelo digital** de 30 estaciones: cada 15 minutos pronostica la hora siguiente (probabilidad de que cada estación quede vacía o llena), propone un plan para el camión de rebalanceo y, una hora después, evalúa el pronóstico contra lo que ocurrió.

Datos abiertos y condiciones de uso: https://ecobici.cdmx.gob.mx/datos-abiertos/

---

## Guía rápida

Lo mínimo para correr el gemelo y abrir el tablero en tu computador (Windows). El detalle de cada paso está en las secciones numeradas más abajo.

### Paso 1 · Descargar e instalar (una sola vez)

1. **Git:** https://git-scm.com/download/win (opciones por defecto). Si no puedes o no quieres instalarlo, mira la sección [Sin Git](#sin-git-descargar-el-proyecto-en-zip).
2. **Python 3.14:** https://www.python.org/downloads/. En el instalador marca **"Add python.exe to PATH"**.
3. **El proyecto.** En PowerShell:
   ```bash
   cd $HOME\Documents
   ```
   ```bash
   git clone https://github.com/ignaburger68-hub/ecobici-gemelo.git
   ```
4. **Los paquetes:**
   ```bash
   py -3.14 -m pip install pandas numpy scipy matplotlib certifi streamlit
   ```

### Paso 2 · Cada vez que trabajes: entrar a la carpeta y traer los datos nuevos

```bash
cd $HOME\Documents\ecobici-gemelo
```
```bash
git pull
```

### Paso 3 · Simular una hora

Una hora que ya pasó (muestra el pronóstico y lo que efectivamente ocurrió):
```bash
py -3.14 gemelo.py hora "2026-11-17 08:00"
```
La próxima hora, desde el estado actual de Ecobici:
```bash
py -3.14 gemelo.py hora --en-vivo
```
Los resultados (mapa, plan del camión, tablas) quedan en `resultados_gemelo/hora_…/`.

### Paso 4 · Abrir el tablero

```bash
py -3.14 -m streamlit run tablero.py
```
Se abre en el navegador (si no, entra a http://localhost:8501). Pestañas:
- **Pronóstico:** simula una hora pasada (*Reproducción*) o la próxima hora (*En vivo*).
- **Rendimiento:** qué tan bien ha pronosticado el gemelo.
- **Tasas:** cómo cambian las tasas durante el día y entre días.

Para cerrarlo: `Ctrl + C` en PowerShell.

### Otros comandos útiles

| Para qué | Comando |
|---|---|
| Medir el rendimiento de una semana | `py -3.14 gemelo.py evaluar --desde 2026-11-23 --hasta 2026-11-27` |
| Elegir los parámetros del modelo | `py -3.14 gemelo.py ajuste --desde 2026-11-17 --hasta 2026-11-20` |
| Gráficos de cómo cambian las tasas | `py -3.14 gemelo.py tasas --desde 2026-11-17 --hasta 2026-11-20` |
| Revisar la cobertura del feed | `py -3.14 diagnostico_feed.py` |

Todos los comandos se corren **dentro de la carpeta `ecobici-gemelo`**. La lista completa está en la [sección 4](#4-comandos-del-gemelo).

---

## Sin Git: descargar el proyecto en ZIP

Si no tienes Git, puedes usar todo igual descargando el proyecto como ZIP.

> **La única diferencia:** los datos **no se actualizan solos**. Quedan congelados en el momento en que descargaste el ZIP. GitHub sigue recolectando, pero tu copia no recibe lo nuevo hasta que vuelvas a descargarla.

### Pasos

1. Instala **Python 3.14** y los paquetes (puntos 2 y 4 del [Paso 1 de la Guía rápida](#paso-1--descargar-e-instalar-una-sola-vez)). Git no hace falta.
2. Entra a https://github.com/ignaburger68-hub/ecobici-gemelo, pulsa el botón verde **«Code»** y luego **«Download ZIP»**.
3. Descomprime el ZIP, por ejemplo en `Documentos`. La carpeta se llama `ecobici-gemelo-main`.
4. En PowerShell, entra a esa carpeta:
   ```bash
   cd $HOME\Documents\ecobici-gemelo-main
   ```
5. Desde ahí funcionan los mismos comandos de la Guía rápida (pasos 3 y 4): `hora`, el tablero, `evaluar`, `tasas`, etc.

### Qué cambia sin Git

| | Con Git | Sin Git (ZIP) |
|---|---|---|
| Lecturas del feed, clima y registro del gemelo en vivo | Se actualizan con `git pull` | Solo hasta el momento de la descarga |
| *Reproducción* (horas pasadas) | Cualquier hora hasta la última lectura de GitHub | Solo horas anteriores a la descarga |
| *En vivo* | Estado actual de Ecobici + lecturas recientes del día | Lee el estado actual de Ecobici, pero el factor del día y la ventana usan las lecturas hasta la descarga, así que el pronóstico es menos preciso |
| Botón «Recargar datos (git pull)» y la casilla «Traer lecturas nuevas» del tablero | Traen las lecturas nuevas | No traen nada nuevo (no dan error): el botón solo vuelve a leer los datos locales |

**Para actualizar los datos sin Git:** descarga de nuevo el ZIP y reemplaza la carpeta. Si guardaste resultados propios en `resultados_gemelo/`, cópialos antes, porque esa carpeta no viene en el ZIP.

---

## 1. Qué corre solo en GitHub

El workflow `.github/workflows/recolectar.yml` corre sin que nadie haga nada. En cada ejecución, que dura unas 5,5 horas:

1. Deja lanzada la ejecución siguiente, que queda en espera y parte apenas termine esta. Así la cadena se sostiene sola. Hay además un respaldo horario (cron).
2. Instala R, Python 3.12 y los paquetes necesarios.
3. Actualiza el clima histórico por hora en `datos/clima/clima_horario.csv` (Open-Meteo).
4. Repite 22 veces:
   - lee el feed una vez por minuto durante 15 minutos (`recolector_ecobici.R`) → `datos/status/AAAA-MM-DD/status_AAAA-MM-DD_HHMM.csv.gz`;
   - corre un ciclo del gemelo (`python gemelo.py ciclo`) → `gemelo_vivo/`;
   - sube todo al repositorio.

Si el gemelo o el clima fallan, **la recolección sigue igual**.

**Para ver el gemelo en vivo**, abre la carpeta [`gemelo_vivo/`](gemelo_vivo/) en GitHub. Su `README.md` se actualiza solo con el mapa, las estaciones con más riesgo, el plan del camión y el puntaje de los pronósticos ya evaluados. El gemelo pronostica entre las 06:00 y las 23:00 (hora de Ciudad de México); fuera de ese horario solo evalúa los pronósticos pendientes.

---

## 2. Preparar el computador (una sola vez)

Las instrucciones son para **Windows**. En Mac o Linux, cambia `py -3.14` por `python3`.

1. **Instala Git:** https://git-scm.com/download/win (opciones por defecto).
2. **Instala Python 3.14:** https://www.python.org/downloads/. En el instalador marca **"Add python.exe to PATH"**.
3. **Descarga el repositorio.** Abre PowerShell y ejecuta:
   ```bash
   cd $HOME\Documents
   ```
   ```bash
   git clone https://github.com/ignaburger68-hub/ecobici-gemelo.git
   ```
4. **Instala los paquetes:**
   ```bash
   py -3.14 -m pip install pandas numpy scipy matplotlib certifi streamlit
   ```

**Cada vez que trabajes**, entra a la carpeta y trae lo último que subió GitHub:
```bash
cd $HOME\Documents\ecobici-gemelo
```
```bash
git pull
```

Todos los comandos de este README se corren **dentro de la carpeta `ecobici-gemelo`**.

---

## 3. Información histórica: qué hay y qué agregar

| Información | Archivo o carpeta | ¿Quién la pone? |
|---|---|---|
| Lecturas del feed (cada minuto) | `datos/status/` | GitHub, solo. Tú haces `git pull` |
| Estaciones de todo el sistema (una vez al día) | `datos/info/` | GitHub, solo |
| Clima por hora desde julio | `datos/clima/clima_horario.csv` | GitHub, solo |
| Las 30 estaciones del gemelo | `estaciones_seleccionadas.csv` | Ya está en el repositorio |
| Perfil base de demanda (cada 15 min) | `perfil_base_15min.csv` | Ya está en el repositorio |
| Relación demanda–clima (factores) | `resultados_clima/factores_clima_gemelo.csv` | Ya está en el repositorio |
| Parámetros del modelo | `config_gemelo.py` | Ya está; se edita a mano si hace falta |
| **Viajes históricos (opcional)** | `public_data_web_*.csv` | **Tú**, solo en tu computador |

### Viajes históricos (opcional)

Solo hacen falta para **recalcular el perfil base**. Sin ellos, el gemelo usa `perfil_base_15min.csv`.

1. Descarga desde https://ecobici.cdmx.gob.mx/datos-abiertos/ los archivos mensuales de viajes de los **3 últimos meses completos** antes de los días que vas a analizar (para noviembre: agosto, septiembre y octubre).
2. Déjalos en la carpeta `ecobici-gemelo`, junto a `gemelo.py`. El código busca archivos que se llamen `public_data_web_*.csv`; si tienen otro nombre o están en otra carpeta, cambia la línea `VIAJES` de `config_gemelo.py`.
3. Corre `py -3.14 gemelo.py preparar` (sección 4).

**No los subas al repositorio**: pesan mucho. El `.gitignore` ya los excluye.

### Clima en tu computador

GitHub mantiene `datos/clima/clima_horario.csv` y te llega con `git pull`. Si lo necesitas antes, o para otras fechas:
```bash
py -3.14 clima_ecobici.py historico 2026-07-01
```
No subas ese archivo con `git push`: GitHub sube el suyo. Si aparece un conflicto al hacer `git pull`, borra tu copia local y vuelve a hacer `git pull`.

---

## 4. Comandos del gemelo

Todos aceptan `--R N` para cambiar el número de réplicas (por defecto 1.000; menos réplicas es más rápido y menos preciso). Los resultados quedan en `resultados_gemelo/`.

### `preparar`: revisar los datos y, si hay viajes, recalcular el perfil base
```bash
py -3.14 gemelo.py preparar
```
Lee viajes, feed y clima, muestra qué datos hay y guarda el perfil base en `resultados_gemelo/perfil_base_15min.csv` y en `perfil_base_15min.csv`. **Solo hace falta si tienes los archivos de viajes**: sin ellos vuelve a escribir el mismo perfil que ya está en el repositorio. Si con viajes el perfil cambia y quieres que GitHub lo use, avísale a quien administre el repositorio, porque este archivo sí está en git.

### `hora`: simular una hora
Una hora pasada (modo reproducción). Muestra el pronóstico, el plan del camión y **lo que efectivamente ocurrió**:
```bash
py -3.14 gemelo.py hora "2026-11-13 07:45"
```
Desde el estado actual del feed y el pronóstico del clima:
```bash
py -3.14 gemelo.py hora --en-vivo
```
Resultados en `resultados_gemelo/hora_AAAA-MM-DD_HHMM/`: `pronostico_estaciones.csv`, `plan_traslados.csv`, `comparacion_planes.csv`, `clima.csv` (clima de la hora y cuánto cambia la demanda), `mapa.png`, `abanico.png`, `resumen.txt` y, si la hora ya pasó, `brier_esta_hora.csv`.

El resumen muestra también **el clima de la hora simulada** (temperatura y cuánto se aleja de lo normal, lluvia y viento) y **su efecto en la demanda**: el factor por el que se multiplican los retiros y las devoluciones, con el detalle por variable. Lo mismo aparece en el tablero y en la página de `gemelo_vivo/`.

### `validar`: comprobar la simulación
```bash
py -3.14 gemelo.py validar --desde 2026-11-17 --hasta 2026-11-20
```
Compara la probabilidad simulada con la exacta (cadena de Markov) y hace el histograma de saltos del feed. `--horas N` cambia cuántas horas se revisan (por defecto 40). Resultados en `resultados_gemelo/validacion/`.

### `ajuste`: elegir los parámetros del modelo
```bash
py -3.14 gemelo.py ajuste --desde 2026-11-17 --hasta 2026-11-20
```
Prueba las combinaciones de `W` (días de la ventana), `m` (peso del perfil base) y `phi` (sobredispersión) definidas en `config_gemelo.py`, y elige la de mejor puntaje de Brier. Guarda:
- `resultados_gemelo/parametros_elegidos.json`: desde ahí, **todos los comandos usan estos parámetros**;
- `resultados_gemelo/persistencia.csv`: la tabla de la referencia "Persistencia".

Usa 500 réplicas por defecto (`R_AJUSTE`) y es el comando más lento.

### `evaluar`: medir qué tan bien pronostica
```bash
py -3.14 gemelo.py evaluar --desde 2026-11-23 --hasta 2026-11-27
```
Compara el **Gemelo** con las referencias **Sin resincronizar** y **Persistencia**, contra lo que ocurrió. Con `--planes` evalúa también el valor de los planes de rebalanceo (bastante más lento). El plan del gemelo se compara con **5 versiones de la regla umbral** (saca bicis de estaciones con ocupación sobre el primer número y las lleva a las que están bajo el segundo: 90/10, 85/15, 80/20, 75/25 y 70/30, configurables en `UMBRALES_REGLA` de `config_gemelo.py`). El resumen marca con ★ la mejor regla del periodo, dice cuántas horas ganó cada una y cuánto le saca el gemelo a la mejor. En `hora` y en el tablero se destaca la mejor regla de esa hora:
```bash
py -3.14 gemelo.py evaluar --desde 2026-11-23 --hasta 2026-11-27 --planes
```
Resultados en `resultados_gemelo/evaluacion/`: `resumen_evaluacion.txt`, `metricas_brier.csv`, `brier_por_hora.png`, `calibracion.png`, `precision_exhaustividad.csv` y, con `--planes`, `planes_por_hora.png` y `planes_resumen.csv`. El tablero los muestra en la pestaña "Rendimiento".

Para probar antes con días ya recolectados (unos 30 s por día):
```bash
py -3.14 gemelo.py evaluar --desde 2026-11-10 --hasta 2026-11-13
```
Si aparece "no hay tabla de persistencia (corre 'ajuste' primero)", es normal: hasta correr `ajuste`, la referencia "Persistencia" se calcula en su versión simple.

### `tasas`: cómo cambian las tasas en el tiempo
```bash
py -3.14 gemelo.py tasas --desde 2026-11-17 --hasta 2026-11-20
```
Calcula, como lo habría hecho el gemelo en cada momento, las tasas de retiros y devoluciones y las compara con los viajes observados. Tres vistas:
1. **A lo largo de cada día** (`dia_AAAA-MM-DD_retiros.png`): perfil base, base + ventana y tasa final (× clima × factor del día) frente a lo observado, y la evolución del factor del día y del clima.
2. **La misma hora en distintos días** (`hora_0800_retiros.png`, …): cómo la ventana aprende de los días anteriores.
3. **Mapa de calor día × hora** (`mapa_calor_retiros.png`): observado ÷ modelo; rojo = más viajes de lo esperado, azul = menos.

Opciones: `--estacion 116` (una estación; por defecto las 30 sumadas) y `--horas 08:00,13:00,18:00` (horas de la vista 2). Resultados (PNG y CSV) en `resultados_gemelo/tasas/` (o `tasas_116/`). Tarda ~1 minuto por semana. Lo mismo se explora en el tablero, pestaña **«Tasas»**.

### `ciclo`: un ciclo del gemelo en vivo
**Lo corre GitHub cada 15 minutos; no lo corras sin `--t0` en tu computador.** Sin `--t0` escribe en `gemelo_vivo/`, el registro oficial. Para probarlo con un instante pasado (escribe en `gemelo_vivo_prueba/`, que no se sube):
```bash
py -3.14 gemelo.py ciclo --t0 "2026-11-13 07:45"
```

### Notas sobre los comandos
- Solo se usan **días hábiles** con al menos 50 % de cobertura del feed (`MIN_COBERTURA_DIA`). Los festivos están en `FESTIVOS` de `config_gemelo.py`; el 16/11/2026 cuenta como festivo.
- Los pronósticos van de 06:00 a 22:45, cada 15 minutos.
- La semilla es fija (`SEMILLA = 2026`): cualquier resultado se reproduce exactamente.
- La primera vez que se leen muchas lecturas tarda 1–2 minutos; después usa la caché `cache_gemelo/`.

---

## 5. Tablero (presentación)

Interfaz web del gemelo, en tu computador:
```bash
py -3.14 -m streamlit run tablero.py
```
Se abre en el navegador (si no, entra a http://localhost:8501).

- **Pestaña "Pronóstico":**
  - *Reproducción*: eliges día y hora ya recolectados. Muestra el pronóstico, el mapa, el plan del camión y, como ya pasó, lo que ocurrió y el puntaje de Brier de esa hora.
    El **día de hoy** también aparece (marcado «hoy») si es hábil y ya tiene lecturas, con horas solo hasta la última lectura: así, por ejemplo, a las 20:00 puedes ver el pronóstico de las 19:00 y compararlo con lo que pasó. Si la hora todavía no termina en los datos, se muestra el pronóstico sin «lo que ocurrió».
  - *En vivo*: lee el feed ahora y pronostica la próxima hora. Con "Actualizar sola" se repite cada 15 minutos; con "git pull" trae antes las lecturas nuevas (solo trae, nunca sube).
- **Pestaña "Rendimiento":**
  - *Pronósticos hechos en tiempo real*: lee `gemelo_vivo/resumen_vivo.csv`, que llega con `git pull`;
  - *Evaluación de la semana*: aparece después de correr `evaluar`.

El botón **«Recargar datos (git pull)»** del panel izquierdo trae las lecturas nuevas de GitHub y vuelve a leer todo, sin reiniciar el tablero. Debajo indica la última lectura cargada.

- **Pestaña "Tasas":** las tres vistas del comando `tasas` (a lo largo del día, la misma hora en distintos días y el mapa de calor), con una breve explicación de cada gráfico. Se elige retiros o devoluciones, las 30 estaciones o una, el día y la hora; los datos se pueden descargar en CSV.

Para cerrar el tablero: `Ctrl + C` en PowerShell.

---

## 6. Otras herramientas

### Diagnóstico de la cobertura del feed
```bash
py -3.14 diagnostico_feed.py
```
Separa los minutos en que **el recolector no leyó** (huecos de GitHub) de los minutos en que **sí leyó, pero la estación no actualizó su reporte**. Muestra la cobertura por día, los huecos más largos y la antigüedad de los reportes.

### Clima
```bash
py -3.14 clima_ecobici.py historico 2026-08-01 2026-10-31
```
```bash
py -3.14 clima_ecobici.py historico --dias 120
```
```bash
py -3.14 clima_ecobici.py actual
```
`historico` acumula en `datos/clima/clima_horario.csv` (y deja una copia por rango en `datos/clima/clima_DESDE_a_HASTA.csv`). `actual` guarda las condiciones de ahora en `datos/clima/clima_actual.csv`; con `--loop` repite cada 15 minutos.

### Leer las lecturas en R
```r
source("leer_datos.R")
s <- leer_status(desde = "2026-11-17")   # todas las lecturas desde esa fecha (UTC)
revisar(s)                               # cobertura y huecos de más de 5 minutos
info <- leer_info()                      # estaciones: nombre, coordenadas, capacidad
```

### Recolector en el computador (sin GitHub)
Requiere R y el paquete `jsonlite` (`install.packages("jsonlite")`).
```bash
Rscript recolector_ecobici.R --loop
```
Lee cada 60 s hasta cerrar la ventana y guarda en `datos/status/status_AAAA-MM-DD.csv`. Sin `--loop` hace una sola lectura. No hace falta mientras GitHub esté recolectando.

---

## 7. Calendario de la investigación

| Fechas | Para qué | Qué correr (desde) |
|---|---|---|
| 17 al 20/11 | Ajustar el modelo | **Sábado 21/11:** `validar` y `ajuste` con `--desde 2026-11-17 --hasta 2026-11-20` |
| 23 al 27/11 | Evaluar el modelo | **Sábado 28/11:** `evaluar --desde 2026-11-23 --hasta 2026-11-27 --planes` |
| Cualquier día | Presentación | `tablero.py` |

Antes de cada análisis: `git pull`. Conviene correr `py -3.14 diagnostico_feed.py` para confirmar que los días a usar tienen buena cobertura.

---

## 8. Administrar la recolección en GitHub

Todo se hace en la pestaña **Actions** del repositorio → **Recolectar Ecobici**.

- **Ver si está funcionando:** debe haber una ejecución *in progress* y otra *pending*. En el repositorio debe aparecer un commit "Lecturas …" cada ~15 minutos. Es normal ver ejecuciones *cancelled*: son esperas reemplazadas por otra más nueva.
- **Lanzar una ejecución a mano:** **Run workflow** → rama `main`. Sirve después de cambiar el workflow, para que la ejecución en espera use la versión nueva (una ejecución en espera usa la versión del workflow de cuando se encoló).
- **Probar cambios sin tocar la recolección:** **Run workflow** sobre otra rama, con pocos bloques (por ejemplo `bloques = 2`, `minutos = 15`). Corre en paralelo, no lanza la siguiente y sube sus datos a esa rama.
- **Detener todo:** "…" → **Disable workflow**, y después cancela la ejecución en espera. Para reanudar: **Enable workflow** y **Run workflow** en `main`.

El repositorio debe ser **público**: así los minutos de Actions son gratis e ilimitados.

---

## 9. Archivos del repositorio

| Archivo / carpeta | Qué es |
|---|---|
| `.github/workflows/recolectar.yml` | Workflow de recolección + gemelo + clima |
| `recolector_ecobici.R` | Lee el feed GBFS y guarda las lecturas |
| `leer_datos.R` | Funciones de R para leer y revisar las lecturas |
| `gemelo.py` | Programa principal del gemelo (comandos de la sección 4) |
| `modelo_gemelo.py` | Modelo: tasas, simulación, pronóstico y planes |
| `datos_gemelo.py` | Lectura de feed, viajes, clima y perfil base |
| `config_gemelo.py` | **Todos los parámetros** (rutas, horarios, réplicas, grillas del ajuste, camión) |
| `clima_ecobici.py` | Descarga del clima (Open-Meteo) |
| `tablero.py` | Tablero Streamlit |
| `tasas_gemelo.py` | Análisis de cómo cambian las tasas (comando `tasas` y pestaña «Tasas») |
| `diagnostico_feed.py` | Diagnóstico de cobertura del feed |
| `estaciones_seleccionadas.csv` | Las 30 estaciones del gemelo |
| `perfil_base_15min.csv` | Perfil base de demanda |
| `resultados_clima/` | Análisis de la relación demanda–clima y sus factores |
| `datos/status/`, `datos/info/`, `datos/clima/` | Datos que sube GitHub |
| `gemelo_vivo/` | Registro del gemelo en vivo (lo escribe GitHub) |
| `resultados_gemelo/`, `cache_gemelo/` | Resultados y caché locales (no se suben) |

---

## 10. Reglas de oro y problemas frecuentes

**Reglas de oro**
1. Empieza siempre con `git pull`.
2. **No hagas `git push`** desde tu computador: los datos los sube GitHub.
3. No corras `gemelo.py ciclo` sin `--t0`.

**Problemas frecuentes**

| Mensaje o síntoma | Qué hacer |
|---|---|
| `'py' no se reconoce…` | Reinstala Python marcando "Add python.exe to PATH" |
| `ModuleNotFoundError: No module named …` | `py -3.14 -m pip install pandas numpy scipy matplotlib certifi streamlit` |
| `git pull` dice que hay cambios locales | `git stash` y de nuevo `git pull` (o borra el archivo local en conflicto) |
| "no encontré datos/clima/clima_horario.csv" | `git pull`; si sigue, `py -3.14 clima_ecobici.py historico 2026-07-01` |
| "tiene poca cobertura del feed; se omite" | Ese día tuvo pocos datos; revísalo con `diagnostico_feed.py` |
| "No hay archivos de viajes … ni perfil base guardado" | Falta `perfil_base_15min.csv`: haz `git pull` |
| No aparecen lecturas nuevas en GitHub | Actions → Recolectar Ecobici: revisa que haya una ejecución *in progress*; si no, **Run workflow** en `main` |
| El tablero no muestra "Rendimiento" | Ver sección 5: se llena con `git pull` (en vivo) y con `evaluar` |
