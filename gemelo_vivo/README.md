# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 16/11/2026 21:14 (hora de Ciudad de México).

## Último pronóstico: 16/11 21:14 a 22:14

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
| 116 Londres-Roma | 18 / 18 | 0.00 | 0.99 | 16-18 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 0.99 | 0.00 | 0-2 |
| 012 Río Lerma - Villalongín | 15 / 15 | 0.00 | 0.99 | 13-15 |
| 255 José Rosas Moreno-Guillermo  | 0 / 28 | 0.99 | 0.00 | 0-2 |
| 003 Reforma - Insurgentes | 0 / 31 | 0.98 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 1 / 31 | 0.76 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 9 / 10 | 0.00 | 0.60 | 7-10 |
| 085 Rosas Moreno - Sullivan | 1 / 14 | 0.45 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 2 / 28 | 0.44 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 3 / 22 | 0.38 | 0.00 | 0-8 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 116 (18/18) a 003 (0/31)
2. Llevar **10 bicis** de 012 (15/15) a 555 (1/31)
3. Llevar **5 bicis** de 048 (9/10) a 255 (0/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

3 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
