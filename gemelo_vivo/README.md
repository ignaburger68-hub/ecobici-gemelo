# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 13:20 (hora de Ciudad de México).

## Último pronóstico: 21/11 13:19 a 14:19

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.8 °C** · sin lluvia · viento 3 km/h · día fin de semana

El clima multiplica los **retiros por 0.93** y las **devoluciones por 0.96** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 048 Independencia - Azueta | 11 / 11 | 0.01 | 0.99 | 6-11 |
| 450 Ramos Arizpe- Av México Teno | 30 / 30 | 0.00 | 0.98 | 25-30 |
| 115 Roma-Dinamarca | 0 / 27 | 0.98 | 0.00 | 0-5 |
| 085 Rosas Moreno - Sullivan | 0 / 15 | 0.98 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 0 / 15 | 0.98 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 0 / 14 | 0.97 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 35 / 35 | 0.00 | 0.97 | 28-35 |
| 260 Av. Juárez-Balderas | 19 / 19 | 0.00 | 0.96 | 13-19 |
| 270 De la República-Ponciano Arr | 26 / 28 | 0.00 | 0.74 | 21-28 |
| 259 Tómas Alva Edison-Ponciano A | 26 / 27 | 0.00 | 0.73 | 23-27 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 450 (30/30) a 115 (0/27)
2. Llevar **8 bicis** de 260 (19/19) a 026 (0/14)
3. Llevar **13 bicis** de 555 (35/35) a 041 (1/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

325 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
