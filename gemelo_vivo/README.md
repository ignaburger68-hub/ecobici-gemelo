# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 16/11/2026 22:25 (hora de Ciudad de México).

## Último pronóstico: 16/11 22:25 a 23:25

![Mapa](ultimo/mapa.png)

### Clima de la hora y su efecto en la demanda

**13.8 °C** · sin lluvia · viento 9 km/h · día fin de semana

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más frío (−3 a −1 °C) | 0.843 | 0.875 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 270 De la República-Ponciano Arr | 0 / 28 | 0.99 | 0.00 | 0-3 |
| 107-108 Tolsa-Balderas | 0 / 52 | 0.99 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 31 | 0.99 | 0.00 | 0-2 |
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 0.99 | 0.00 | 0-3 |
| 256 Gómez Farías-Sadi Carnot | 1 / 17 | 0.69 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 2 / 8 | 0.41 | 0.01 | 0-4 |
| 085 Rosas Moreno - Sullivan | 1 / 14 | 0.38 | 0.00 | 0-3 |
| 119 Turín-Abraham González | 3 / 25 | 0.23 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 3 / 26 | 0.22 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 3 / 10 | 0.21 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 116 (16/18) a 270 (0/28)
2. Llevar **9 bicis** de 112 (16/20) a 555 (0/31)
3. Llevar **10 bicis** de 114 (15/20) a 003 (0/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

8 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
