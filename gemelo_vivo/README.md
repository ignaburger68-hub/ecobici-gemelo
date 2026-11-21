# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 13:05 (hora de Ciudad de México).

## Último pronóstico: 21/11 13:05 a 14:05

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.8 °C** · sin lluvia · viento 3 km/h · día fin de semana

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
| 115 Roma-Dinamarca | 0 / 27 | 0.98 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 0 / 14 | 0.98 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 35 / 35 | 0.00 | 0.97 | 28-35 |
| 270 De la República-Ponciano Arr | 28 / 29 | 0.00 | 0.82 | 23-29 |
| 259 Tómas Alva Edison-Ponciano A | 26 / 27 | 0.00 | 0.74 | 23-27 |
| 085 Rosas Moreno - Sullivan | 1 / 15 | 0.71 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 2 / 15 | 0.67 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 18 / 20 | 0.00 | 0.59 | 13-20 |
| 048 Independencia - Azueta | 9 / 11 | 0.01 | 0.48 | 5-11 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 555 (35/35) a 026 (0/14)
2. Llevar **14 bicis** de 270 (28/29) a 115 (0/27)
3. Llevar **7 bicis** de 450 (30/30) a 086 (2/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

324 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
