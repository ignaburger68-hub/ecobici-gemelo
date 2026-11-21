# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 12:09 (hora de Ciudad de México).

## Último pronóstico: 21/11 12:08 a 13:08

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.5 °C** · sin lluvia · viento 3 km/h · día fin de semana

El clima multiplica los **retiros por 0.92** y las **devoluciones por 0.94** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 450 Ramos Arizpe- Av México Teno | 30 / 30 | 0.00 | 1.00 | 27-30 |
| 270 De la República-Ponciano Arr | 29 / 30 | 0.00 | 0.91 | 24-30 |
| 260 Av. Juárez-Balderas | 17 / 20 | 0.00 | 0.78 | 15-20 |
| 555 Ribera de San Cosme - Insurg | 33 / 35 | 0.00 | 0.71 | 30-35 |
| 119 Turín-Abraham González | 1 / 28 | 0.56 | 0.00 | 1-8 |
| 010 Reforma - Ramírez | 3 / 25 | 0.53 | 0.00 | 0-8 |
| 026 Reforma - Versalles | 2 / 14 | 0.52 | 0.01 | 0-9 |
| 259 Tómas Alva Edison-Ponciano A | 25 / 27 | 0.00 | 0.51 | 23-27 |
| 020 Reforma- Río Támesis | 2 / 23 | 0.51 | 0.00 | 1-10 |
| 085 Rosas Moreno - Sullivan | 2 / 15 | 0.42 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 270 (29/30) a 010 (3/25)
2. Llevar **10 bicis** de 260 (17/20) a 020 (2/23)
3. Llevar **5 bicis** de 450 (30/30) a 026 (2/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

320 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
