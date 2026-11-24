# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 19:46 (hora de Ciudad de México).

## Último pronóstico: 23/11 19:46 a 20:46

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.1 °C** · lluvia 0.1 mm/h · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.85** y las **devoluciones por 0.89** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 026 Reforma - Versalles | 11 / 11 | 0.00 | 1.00 | 7-11 |
| 450 Ramos Arizpe- Av México Teno | 29 / 29 | 0.00 | 0.99 | 26-29 |
| 118 Liverpool-Dinamarca | 0 / 18 | 0.99 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 27 / 27 | 0.00 | 0.98 | 21-27 |
| 048 Independencia - Azueta | 9 / 9 | 0.00 | 0.98 | 5-9 |
| 114 Lucerna-Abraham González | 0 / 23 | 0.94 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 18 / 20 | 0.00 | 0.83 | 16-20 |
| 113 General Prim-Versalles | 1 / 13 | 0.76 | 0.01 | 0-5 |
| 029 Reforma - Bucareli | 29 / 32 | 0.00 | 0.52 | 23-32 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 555 (27/27) a 118 (0/18)
2. Llevar **14 bicis** de 450 (29/29) a 114 (0/23)
3. Llevar **7 bicis** de 026 (11/11) a 113 (1/13)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

494 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
