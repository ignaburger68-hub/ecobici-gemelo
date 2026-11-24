# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 20:43 (hora de Ciudad de México).

## Último pronóstico: 23/11 20:43 a 21:43

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.6 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.89** y las **devoluciones por 0.91** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 260 Av. Juárez-Balderas | 21 / 21 | 0.00 | 1.00 | 19-21 |
| 048 Independencia - Azueta | 11 / 11 | 0.00 | 1.00 | 9-11 |
| 117 Londres-Nápoles | 0 / 30 | 0.96 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 13 / 14 | 0.00 | 0.95 | 11-14 |
| 086 Sullivan-Insurgentes | 15 / 17 | 0.00 | 0.90 | 14-17 |
| 555 Ribera de San Cosme - Insurg | 31 / 34 | 0.00 | 0.90 | 31-34 |
| 450 Ramos Arizpe- Av México Teno | 29 / 31 | 0.00 | 0.87 | 30-31 |
| 029 Reforma - Bucareli | 28 / 32 | 0.00 | 0.83 | 29-32 |
| 256 Gómez Farías-Sadi Carnot | 20 / 22 | 0.00 | 0.76 | 18-22 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 260 (21/21) a 117 (0/30)
2. Llevar **20 bicis** de 555 (31/34) a 031 (1/36)
3. Llevar **20 bicis** de 029 (28/32) a 107-108 (6/55)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

498 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.117 | 0.031 |
| Sin resincronizar | 0.251 | 0.088 |
| Persistencia | 0.287 | 0.060 |
| Persistencia 0/1 | 0.287 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
