# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 17:33 (hora de Ciudad de México).

## Último pronóstico: 26/11 17:32 a 18:32

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.7 °C** · sin lluvia · viento 7 km/h · día hábil

El clima multiplica los **retiros por 0.58** y las **devoluciones por 0.65** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 029 Reforma - Bucareli | 30 / 30 | 0.00 | 1.00 | 24-30 |
| 260 Av. Juárez-Balderas | 21 / 21 | 0.00 | 1.00 | 17-21 |
| 255 José Rosas Moreno-Guillermo  | 0 / 33 | 0.97 | 0.00 | 0-7 |
| 008 Reforma - General Prim | 3 / 8 | 0.89 | 0.05 | 0-2 |
| 270 De la República-Ponciano Arr | 0 / 7 | 0.76 | 0.89 | 6-7 |
| 048 Independencia - Azueta | 7 / 8 | 0.03 | 0.89 | 4-8 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 26 | 0.85 | 0.00 | 0-8 |
| 119 Turín-Abraham González | 2 / 24 | 0.80 | 0.00 | 1-9 |
| 085 Rosas Moreno - Sullivan | 3 / 13 | 0.79 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 029 (30/30) a 031 (11/27)
2. Llevar **16 bicis** de 260 (21/21) a 119 (2/24)
3. Llevar **5 bicis** de 048 (7/8) a 085 (3/13)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

698 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.036 |
| Sin resincronizar | 0.250 | 0.081 |
| Persistencia | 0.258 | 0.061 |
| Persistencia 0/1 | 0.258 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
