# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 16:08 (hora de Ciudad de México).

## Último pronóstico: 22/11 16:07 a 17:07

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.9 °C** · lluvia 0.3 mm/h · viento 9 km/h · día fin de semana

El clima multiplica los **retiros por 0.61** y las **devoluciones por 0.66** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | llovió en las 3 h previas | 0.743 | 0.789 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 115 Roma-Dinamarca | 1 / 25 | 0.78 | 0.00 | 0-5 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.66 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 10 / 11 | 0.01 | 0.64 | 6-11 |
| 031 Hamburgo - Insurgentes | 3 / 35 | 0.43 | 0.00 | 0-9 |
| 012 Río Lerma - Villalongín | 3 / 13 | 0.38 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 4 / 31 | 0.38 | 0.00 | 0-8 |
| 086 Sullivan-Insurgentes | 3 / 12 | 0.34 | 0.02 | 0-7 |
| 116 Londres-Roma | 3 / 23 | 0.32 | 0.00 | 1-8 |
| 003 Reforma - Insurgentes | 3 / 29 | 0.32 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 9 / 11 | 0.00 | 0.29 | 5-11 |

### Plan recomendado del camión

1. Llevar **5 bicis** de 048 (10/11) a 115 (1/25)
2. Llevar **10 bicis** de 270 (20/27) a 031 (3/35)
3. Llevar **7 bicis** de 259 (23/26) a 255 (1/33)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

408 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
