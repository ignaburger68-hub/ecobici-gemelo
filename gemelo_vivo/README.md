# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 19:18 (hora de Ciudad de México).

## Último pronóstico: 23/11 19:17 a 20:17

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.6 °C** · lluvia 0.1 mm/h · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.80** y las **devoluciones por 0.85** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 555 Ribera de San Cosme - Insurg | 27 / 27 | 0.00 | 1.00 | 17-27 |
| 119 Turín-Abraham González | 0 / 28 | 1.00 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 0 / 18 | 0.99 | 0.00 | 0-3 |
| 113 General Prim-Versalles | 0 / 14 | 0.99 | 0.00 | 0-6 |
| 086 Sullivan-Insurgentes | 0 / 14 | 0.99 | 0.01 | 0-6 |
| 012 Río Lerma - Villalongín | 0 / 13 | 0.99 | 0.01 | 0-5 |
| 020 Reforma- Río Támesis | 0 / 20 | 0.99 | 0.00 | 0-8 |
| 008 Reforma - General Prim | 0 / 15 | 0.99 | 0.00 | 0-7 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 0.98 | 14-20 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 555 (27/27) a 119 (0/28)
2. Llevar **13 bicis** de 260 (20/20) a 118 (0/18)
3. Llevar **15 bicis** de 029 (31/32) a 003 (1/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

492 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.031 |
| Sin resincronizar | 0.252 | 0.087 |
| Persistencia | 0.290 | 0.059 |
| Persistencia 0/1 | 0.290 | 0.059 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
