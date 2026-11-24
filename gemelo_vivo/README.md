# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 06:10 (hora de Ciudad de México).

## Último pronóstico: 24/11 06:10 a 07:10

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**10.6 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 114 Lucerna-Abraham González | 0 / 16 | 0.99 | 0.00 | 0-2 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 0.99 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 11 / 11 | 0.01 | 0.97 | 5-11 |
| 116 Londres-Roma | 0 / 20 | 0.97 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 1 / 16 | 0.94 | 0.00 | 0-1 |
| 029 Reforma - Bucareli | 0 / 25 | 0.94 | 0.00 | 2-10 |
| 041 Reforma - Av. de la Repúblic | 1 / 32 | 0.79 | 0.00 | 0-4 |
| 085 Rosas Moreno - Sullivan | 8 / 9 | 0.02 | 0.57 | 3-9 |
| 555 Ribera de San Cosme - Insurg | 10 / 32 | 0.53 | 0.00 | 0-8 |
| 115 Roma-Dinamarca | 1 / 24 | 0.46 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 450 (30/31) a 086 (1/16)
2. Llevar **16 bicis** de 263 (28/29) a 555 (10/32)
3. Llevar **5 bicis** de 048 (11/11) a 041 (1/32)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

511 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.032 |
| Sin resincronizar | 0.245 | 0.087 |
| Persistencia | 0.278 | 0.060 |
| Persistencia 0/1 | 0.278 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
