# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 08:07 (hora de Ciudad de México).

## Último pronóstico: 17/11 08:06 a 09:06

![Mapa](ultimo/mapa.png)

### Clima de la hora y su efecto en la demanda

**12.7 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 1.00 | 0.00 | 0-1 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 24 | 1.00 | 0.00 | 0-1 |
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 1.00 | 0.00 | 0-1 |
| 107-108 Tolsa-Balderas | 1 / 55 | 1.00 | 0.00 | 0-1 |
| 255 José Rosas Moreno-Guillermo  | 0 / 28 | 1.00 | 0.00 | 0-2 |
| 450 Ramos Arizpe- Av México Teno | 1 / 28 | 1.00 | 0.00 | 0-1 |
| 085 Rosas Moreno - Sullivan | 0 / 14 | 1.00 | 0.00 | 0-3 |
| 119 Turín-Abraham González | 0 / 25 | 0.99 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 2 / 26 | 0.99 | 0.00 | 0-1 |
| 026 Reforma - Versalles | 10 / 10 | 0.01 | 0.99 | 5-10 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 117 (26/29) a 555 (0/31)
2. Llevar **10 bicis** de 026 (10/10) a 107-108 (1/55)
3. Llevar **16 bicis** de 029 (23/28) a 259 (1/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

19 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.069 | 0.054 |
| Sin resincronizar | 0.124 | 0.060 |
| Persistencia | 0.274 | 0.141 |
| Persistencia 0/1 | 0.274 | 0.141 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
