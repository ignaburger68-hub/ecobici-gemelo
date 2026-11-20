# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 14:48 (hora de Ciudad de México).

## Último pronóstico: 20/11 14:48 a 15:48

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.9 °C** · sin lluvia · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.83** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 020 Reforma- Río Támesis | 0 / 21 | 0.99 | 0.00 | 0-4 |
| 116 Londres-Roma | 22 / 22 | 0.00 | 0.98 | 14-21 |
| 255 José Rosas Moreno-Guillermo  | 0 / 33 | 0.98 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 19 / 19 | 0.00 | 0.98 | 11-19 |
| 012 Río Lerma - Villalongín | 0 / 14 | 0.97 | 0.00 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 0 / 29 | 0.97 | 0.00 | 0-8 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.96 | 8-15 |
| 008 Reforma - General Prim | 1 / 16 | 0.94 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 2 / 25 | 0.80 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 116 (22/22) a 020 (0/21)
2. Llevar **9 bicis** de 118 (19/19) a 008 (1/16)
3. Llevar **15 bicis** de 031 (33/34) a 010 (2/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

260 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.035 |
| Sin resincronizar | 0.273 | 0.091 |
| Persistencia | 0.310 | 0.067 |
| Persistencia 0/1 | 0.310 | 0.067 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
