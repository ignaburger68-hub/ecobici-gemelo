# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 26/11/2026 19:12 (hora de Ciudad de México).

## Último pronóstico: 26/11 19:12 a 20:12

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.7 °C** · lluvia 0.2 mm/h · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.64** y las **devoluciones por 0.70** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | mucho más frío (< −3 °C) | 0.840 | 0.889 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 260 Av. Juárez-Balderas | 21 / 21 | 0.00 | 1.00 | 17-21 |
| 048 Independencia - Azueta | 10 / 10 | 0.01 | 0.99 | 6-10 |
| 029 Reforma - Bucareli | 33 / 33 | 0.00 | 0.99 | 26-33 |
| 086 Sullivan-Insurgentes | 0 / 15 | 0.98 | 0.01 | 0-9 |
| 115 Roma-Dinamarca | 0 / 24 | 0.98 | 0.00 | 0-8 |
| 085 Rosas Moreno - Sullivan | 0 / 13 | 0.98 | 0.00 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 30 / 31 | 0.00 | 0.97 | 26-31 |
| 113 General Prim-Versalles | 1 / 15 | 0.97 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 0 / 7 | 0.73 | 0.94 | 7-7 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 260 (21/21) a 115 (0/24)
2. Llevar **12 bicis** de 029 (33/33) a 113 (1/15)
3. Llevar **10 bicis** de 041 (30/31) a 086 (0/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

705 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.036 |
| Sin resincronizar | 0.249 | 0.081 |
| Persistencia | 0.258 | 0.061 |
| Persistencia 0/1 | 0.258 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
