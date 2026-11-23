# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 17:08 (hora de Ciudad de México).

## Último pronóstico: 23/11 17:08 a 18:08

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.8 °C** · sin lluvia · viento 7 km/h · día hábil

El clima multiplica los **retiros por 0.72** y las **devoluciones por 0.78** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 010 Reforma - Ramírez | 0 / 26 | 1.00 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 19 | 1.00 | 0.00 | 0-4 |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 113 General Prim-Versalles | 0 / 14 | 1.00 | 0.00 | 0-3 |
| 012 Río Lerma - Villalongín | 0 / 14 | 0.99 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 1 / 27 | 0.95 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 1 / 24 | 0.95 | 0.00 | 0-2 |
| 026 Reforma - Versalles | 2 / 11 | 0.85 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 3 / 26 | 0.75 | 0.00 | 0-6 |
| 255 José Rosas Moreno-Guillermo  | 2 / 33 | 0.75 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 029 (24/33) a 010 (0/26)
2. Llevar **11 bicis** de 116 (15/22) a 115 (1/24)
3. Llevar **7 bicis** de 098 (9/28) a 020 (0/19)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

483 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.031 |
| Sin resincronizar | 0.254 | 0.087 |
| Persistencia | 0.289 | 0.060 |
| Persistencia 0/1 | 0.289 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
