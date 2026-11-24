# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 20:00 (hora de Ciudad de México).

## Último pronóstico: 23/11 20:00 a 21:00

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.1 °C** · lluvia 0.1 mm/h · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.87** y las **devoluciones por 0.91** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 555 Ribera de San Cosme - Insurg | 28 / 28 | 0.00 | 1.00 | 23-28 |
| 450 Ramos Arizpe- Av México Teno | 29 / 29 | 0.00 | 0.99 | 27-29 |
| 048 Independencia - Azueta | 9 / 9 | 0.00 | 0.99 | 6-9 |
| 026 Reforma - Versalles | 11 / 11 | 0.00 | 0.99 | 8-11 |
| 118 Liverpool-Dinamarca | 0 / 18 | 0.98 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 19 / 21 | 0.00 | 0.90 | 19-21 |
| 117 Londres-Nápoles | 2 / 26 | 0.59 | 0.00 | 0-6 |
| 029 Reforma - Bucareli | 29 / 32 | 0.00 | 0.58 | 26-32 |
| 114 Lucerna-Abraham González | 1 / 23 | 0.56 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 555 (28/28) a 118 (0/18)
2. Llevar **14 bicis** de 260 (19/21) a 117 (2/26)
3. Llevar **13 bicis** de 450 (29/29) a 114 (1/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

495 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.031 |
| Sin resincronizar | 0.252 | 0.087 |
| Persistencia | 0.289 | 0.060 |
| Persistencia 0/1 | 0.289 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
