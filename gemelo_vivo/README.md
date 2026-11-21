# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 13:34 (hora de Ciudad de México).

## Último pronóstico: 21/11 13:34 a 14:34

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**23.4 °C** · sin lluvia · viento 3 km/h · día fin de semana

El clima multiplica los **retiros por 0.95** y las **devoluciones por 0.98** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 450 Ramos Arizpe- Av México Teno | 30 / 30 | 0.00 | 0.98 | 25-30 |
| 026 Reforma - Versalles | 0 / 14 | 0.97 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 35 / 35 | 0.00 | 0.97 | 28-35 |
| 041 Reforma - Av. de la Repúblic | 0 / 31 | 0.90 | 0.00 | 1-11 |
| 270 De la República-Ponciano Arr | 30 / 31 | 0.00 | 0.88 | 25-31 |
| 085 Rosas Moreno - Sullivan | 1 / 15 | 0.73 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 18 / 20 | 0.00 | 0.69 | 13-20 |
| 048 Independencia - Azueta | 9 / 11 | 0.02 | 0.64 | 5-11 |
| 115 Roma-Dinamarca | 2 / 27 | 0.58 | 0.00 | 0-7 |
| 119 Turín-Abraham González | 2 / 29 | 0.53 | 0.00 | 0-9 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 270 (30/31) a 041 (0/31)
2. Llevar **8 bicis** de 450 (30/30) a 026 (0/14)
3. Llevar **13 bicis** de 555 (35/35) a 010 (3/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

326 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
