# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 16/11/2026 21:00 (hora de Ciudad de México).

## Último pronóstico: 16/11 21:00 a 22:00

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
| 255 José Rosas Moreno-Guillermo  | 0 / 28 | 0.99 | 0.00 | 0-2 |
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 0.98 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 11 / 12 | 0.00 | 0.68 | 7-12 |
| 003 Reforma - Insurgentes | 1 / 30 | 0.68 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 1 / 19 | 0.58 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 2 / 22 | 0.57 | 0.00 | 0-8 |
| 048 Independencia - Azueta | 9 / 10 | 0.00 | 0.56 | 6-10 |
| 118 Liverpool-Dinamarca | 15 / 16 | 0.00 | 0.36 | 13-16 |
| 012 Río Lerma - Villalongín | 13 / 15 | 0.00 | 0.31 | 11-15 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 116 (18/18) a 555 (0/31)
2. Llevar **6 bicis** de 020 (11/12) a 041 (2/22)
3. Llevar **4 bicis** de 048 (9/10) a 255 (0/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

2 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
