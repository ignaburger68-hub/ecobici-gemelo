# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 20:57 (hora de Ciudad de México).

## Último pronóstico: 23/11 20:57 a 21:57

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.6 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.90** y las **devoluciones por 0.92** (1,00 = sin efecto).

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
| 086 Sullivan-Insurgentes | 16 / 16 | 0.00 | 1.00 | 13-16 |
| 048 Independencia - Azueta | 11 / 11 | 0.00 | 1.00 | 10-11 |
| 026 Reforma - Versalles | 13 / 13 | 0.00 | 0.99 | 9-13 |
| 450 Ramos Arizpe- Av México Teno | 29 / 31 | 0.00 | 0.88 | 29-31 |
| 555 Ribera de San Cosme - Insurg | 31 / 34 | 0.00 | 0.82 | 31-34 |
| 256 Gómez Farías-Sadi Carnot | 20 / 22 | 0.00 | 0.71 | 18-22 |
| 113 General Prim-Versalles | 11 / 15 | 0.00 | 0.56 | 11-15 |
| 117 Londres-Nápoles | 1 / 30 | 0.56 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 086 (16/16) a 117 (1/30)
2. Llevar **20 bicis** de 555 (31/34) a 031 (2/36)
3. Llevar **12 bicis** de 260 (21/21) a 020 (5/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

499 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
