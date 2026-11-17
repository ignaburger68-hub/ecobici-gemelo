# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 17:39 (hora de Ciudad de México).

## Último pronóstico: 17/11 17:39 a 18:39

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**17.6 °C** · sin lluvia · viento 7 km/h · día hábil

El clima multiplica los **retiros por 0.77** y las **devoluciones por 0.81** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 010 Reforma - Ramírez | 0 / 26 | 1.00 | 0.00 | 0-2 |
| 031 Hamburgo - Insurgentes | 0 / 26 | 1.00 | 0.00 | 0-1 |
| 117 Londres-Nápoles | 0 / 29 | 1.00 | 0.00 | 0-1 |
| 008 Reforma - General Prim | 0 / 17 | 1.00 | 0.00 | 0-2 |
| 020 Reforma- Río Támesis | 0 / 9 | 1.00 | 0.01 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 30 | 1.00 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 0 / 14 | 1.00 | 0.00 | 0-2 |
| 115 Roma-Dinamarca | 2 / 23 | 0.99 | 0.00 | 0-2 |
| 085 Rosas Moreno - Sullivan | 0 / 13 | 0.99 | 0.00 | 0-4 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 0.99 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 555 (24/30) a 031 (0/26)
2. Llevar **15 bicis** de 260 (18/18) a 117 (0/29)
3. Llevar **10 bicis** de 107-108 (13/44) a 115 (2/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

59 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.151 | 0.027 |
| Sin resincronizar | 0.280 | 0.091 |
| Persistencia | 0.347 | 0.047 |
| Persistencia 0/1 | 0.347 | 0.047 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
