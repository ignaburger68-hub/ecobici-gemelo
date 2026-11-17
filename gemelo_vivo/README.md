# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 16/11/2026 21:28 (hora de Ciudad de México).

## Último pronóstico: 16/11 21:28 a 22:28

![Mapa](ultimo/mapa.png)

### Clima de la hora y su efecto en la demanda

**14.3 °C** · sin lluvia · viento 8 km/h · día fin de semana

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
| 003 Reforma - Insurgentes | 0 / 31 | 0.98 | 0.00 | 0-4 |
| 116 Londres-Roma | 17 / 18 | 0.00 | 0.73 | 15-18 |
| 256 Gómez Farías-Sadi Carnot | 1 / 19 | 0.59 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 9 / 10 | 0.00 | 0.59 | 6-10 |
| 012 Río Lerma - Villalongín | 14 / 15 | 0.00 | 0.59 | 12-15 |
| 255 José Rosas Moreno-Guillermo  | 1 / 28 | 0.56 | 0.00 | 0-3 |
| 010 Reforma - Ramírez | 2 / 27 | 0.42 | 0.00 | 0-5 |
| 085 Rosas Moreno - Sullivan | 1 / 13 | 0.42 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 3 / 28 | 0.26 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 116 (17/18) a 555 (0/31)
2. Llevar **5 bicis** de 048 (9/10) a 003 (0/31)
3. Llevar **6 bicis** de 012 (14/15) a 256 (1/19)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

4 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
