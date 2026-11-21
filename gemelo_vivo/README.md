# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 10:58 (hora de Ciudad de México).

## Último pronóstico: 21/11 10:57 a 11:57

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.6 °C** · sin lluvia · viento 4 km/h · día fin de semana

El clima multiplica los **retiros por 0.93** y las **devoluciones por 0.96** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 118 Liverpool-Dinamarca | 0 / 18 | 0.99 | 0.00 | 0-3 |
| 112 Av. Morelos-Abraham González | 1 / 22 | 0.83 | 0.00 | 0-4 |
| 116 Londres-Roma | 2 / 23 | 0.75 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 2 / 33 | 0.62 | 0.00 | 0-3 |
| 085 Rosas Moreno - Sullivan | 2 / 15 | 0.62 | 0.00 | 0-4 |
| 119 Turín-Abraham González | 2 / 29 | 0.60 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 2 / 15 | 0.58 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 3 / 23 | 0.55 | 0.00 | 0-8 |
| 086 Sullivan-Insurgentes | 2 / 17 | 0.54 | 0.00 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 4 / 31 | 0.51 | 0.00 | 1-12 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 270 (24/29) a 116 (2/23)
2. Llevar **6 bicis** de 260 (14/21) a 118 (0/18)
3. Llevar **10 bicis** de 450 (25/30) a 041 (4/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

315 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.259 | 0.091 |
| Persistencia | 0.296 | 0.066 |
| Persistencia 0/1 | 0.296 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
