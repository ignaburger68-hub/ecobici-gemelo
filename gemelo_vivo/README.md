# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 07:52 (hora de Ciudad de México).

## Último pronóstico: 17/11 07:52 a 08:52

![Mapa](ultimo/mapa.png)

### Clima de la hora y su efecto en la demanda

**12.7 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.84** y las **devoluciones por 0.86** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 113 General Prim-Versalles | 10 / 10 | 0.00 | 1.00 | 8-10 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 1.00 | 0.00 | 0-1 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 1.00 | 0.00 | 0-1 |
| 450 Ramos Arizpe- Av México Teno | 1 / 28 | 1.00 | 0.00 | 0-1 |
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 1.00 | 0.00 | 0-1 |
| 086 Sullivan-Insurgentes | 0 / 7 | 1.00 | 0.02 | 0-3 |
| 255 José Rosas Moreno-Guillermo  | 0 / 28 | 1.00 | 0.00 | 0-2 |
| 085 Rosas Moreno - Sullivan | 0 / 13 | 1.00 | 0.00 | 0-3 |
| 107-108 Tolsa-Balderas | 2 / 53 | 1.00 | 0.00 | 0-2 |
| 026 Reforma - Versalles | 10 / 10 | 0.01 | 1.00 | 6-10 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 117 (17/30) a 107-108 (2/53)
2. Llevar **10 bicis** de 113 (10/10) a 450 (1/28)
3. Llevar **10 bicis** de 026 (10/10) a 259 (0/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

18 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.063 | 0.061 |
| Sin resincronizar | 0.124 | 0.064 |
| Persistencia | 0.250 | 0.148 |
| Persistencia 0/1 | 0.250 | 0.148 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
