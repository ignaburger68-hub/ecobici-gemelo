# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 16/11/2026 21:43 (hora de Ciudad de México).

## Último pronóstico: 16/11 21:42 a 22:42

![Mapa](ultimo/mapa.png)

### Clima de la hora y su efecto en la demanda

**13.8 °C** · sin lluvia · viento 9 km/h · día fin de semana

El clima multiplica los **retiros por 0.78** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más frío (−3 a −1 °C) | 0.843 | 0.875 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 0.99 | 0.00 | 0-3 |
| 116 Londres-Roma | 18 / 18 | 0.00 | 0.99 | 14-18 |
| 003 Reforma - Insurgentes | 0 / 31 | 0.98 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 1 / 27 | 0.65 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 1 / 19 | 0.62 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 9 / 10 | 0.00 | 0.56 | 7-10 |
| 012 Río Lerma - Villalongín | 14 / 15 | 0.00 | 0.54 | 12-15 |
| 270 De la República-Ponciano Arr | 2 / 28 | 0.47 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 15 / 16 | 0.00 | 0.45 | 13-16 |
| 113 General Prim-Versalles | 8 / 10 | 0.00 | 0.26 | 6-10 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 116 (18/18) a 555 (0/31)
2. Llevar **5 bicis** de 048 (9/10) a 003 (0/31)
3. Llevar **9 bicis** de 012 (14/15) a 010 (1/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

5 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | nan | nan |
| Sin resincronizar | nan | nan |
| Persistencia | nan | nan |
| Persistencia 0/1 | nan | nan |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
