# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 19:41 (hora de Ciudad de México).

## Último pronóstico: 18/11 19:41 a 20:41

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.6 °C** · sin lluvia · viento 10 km/h · día hábil

El clima multiplica los **retiros por 0.78** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 118 Liverpool-Dinamarca | 0 / 12 | 1.00 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 0 / 29 | 0.99 | 0.00 | 0-3 |
| 260 Av. Juárez-Balderas | 19 / 19 | 0.00 | 0.99 | 13-19 |
| 020 Reforma- Río Támesis | 0 / 10 | 0.99 | 0.01 | 0-4 |
| 116 Londres-Roma | 0 / 17 | 0.98 | 0.00 | 0-5 |
| 117 Londres-Nápoles | 0 / 28 | 0.98 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 0 / 24 | 0.97 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 0 / 9 | 0.96 | 0.11 | 0-4 |
| 086 Sullivan-Insurgentes | 1 / 8 | 0.90 | 0.13 | 0-6 |
| 114 Lucerna-Abraham González | 1 / 17 | 0.81 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 260 (19/19) a 003 (0/29)
2. Llevar **10 bicis** de 555 (23/27) a 118 (0/12)
3. Llevar **14 bicis** de 255 (22/30) a 041 (0/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

138 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.128 | 0.033 |
| Sin resincronizar | 0.306 | 0.085 |
| Persistencia | 0.346 | 0.067 |
| Persistencia 0/1 | 0.346 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
