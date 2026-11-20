# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 15:02 (hora de Ciudad de México).

## Último pronóstico: 20/11 15:02 a 16:02

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.9 °C** · sin lluvia · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 020 Reforma- Río Támesis | 0 / 21 | 0.99 | 0.00 | 0-5 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.99 | 0.00 | 0-6 |
| 116 Londres-Roma | 22 / 22 | 0.00 | 0.96 | 15-22 |
| 041 Reforma - Av. de la Repúblic | 0 / 28 | 0.96 | 0.00 | 0-8 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.93 | 9-15 |
| 008 Reforma - General Prim | 1 / 16 | 0.85 | 0.00 | 0-4 |
| 031 Hamburgo - Insurgentes | 33 / 34 | 0.00 | 0.85 | 29-34 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.78 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 1 / 15 | 0.76 | 0.01 | 0-9 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 031 (33/34) a 020 (0/21)
2. Llevar **10 bicis** de 116 (22/22) a 112 (0/20)
3. Llevar **8 bicis** de 113 (15/15) a 255 (1/33)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

261 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.035 |
| Sin resincronizar | 0.272 | 0.091 |
| Persistencia | 0.310 | 0.067 |
| Persistencia 0/1 | 0.310 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
