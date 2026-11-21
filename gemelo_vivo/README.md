# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 12:51 (hora de Ciudad de México).

## Último pronóstico: 21/11 12:51 a 13:51

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.9 °C** · sin lluvia · viento 2 km/h · día fin de semana

El clima multiplica los **retiros por 0.92** y las **devoluciones por 0.94** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 450 Ramos Arizpe- Av México Teno | 30 / 30 | 0.00 | 0.99 | 26-30 |
| 118 Liverpool-Dinamarca | 0 / 18 | 0.98 | 0.00 | 0-3 |
| 270 De la República-Ponciano Arr | 28 / 29 | 0.00 | 0.87 | 23-29 |
| 259 Tómas Alva Edison-Ponciano A | 26 / 27 | 0.00 | 0.73 | 23-27 |
| 041 Reforma - Av. de la Repúblic | 1 / 31 | 0.73 | 0.00 | 2-14 |
| 026 Reforma - Versalles | 1 / 14 | 0.72 | 0.00 | 0-6 |
| 115 Roma-Dinamarca | 1 / 27 | 0.69 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 33 / 35 | 0.00 | 0.65 | 28-35 |
| 085 Rosas Moreno - Sullivan | 2 / 15 | 0.48 | 0.00 | 0-5 |
| 119 Turín-Abraham González | 2 / 28 | 0.40 | 0.00 | 0-8 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 270 (28/29) a 118 (0/18)
2. Llevar **11 bicis** de 450 (30/30) a 041 (1/31)
3. Llevar **7 bicis** de 555 (33/35) a 026 (1/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

323 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
