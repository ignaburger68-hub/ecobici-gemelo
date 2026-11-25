# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 21:25 (hora de Ciudad de México).

## Último pronóstico: 24/11 21:25 a 22:25

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.3 °C** · lluvia 0.8 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.54** y las **devoluciones por 0.61** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 450 Ramos Arizpe- Av México Teno | 30 / 30 | 0.00 | 1.00 | 28-30 |
| 113 General Prim-Versalles | 0 / 15 | 0.99 | 0.00 | 0-4 |
| 116 Londres-Roma | 0 / 23 | 0.97 | 0.00 | 0-6 |
| 555 Ribera de San Cosme - Insurg | 27 / 29 | 0.00 | 0.79 | 22-29 |
| 098 Emilio Dondé-Av. Balderas | 29 / 31 | 0.00 | 0.79 | 29-31 |
| 260 Av. Juárez-Balderas | 18 / 21 | 0.00 | 0.61 | 16-21 |
| 086 Sullivan-Insurgentes | 11 / 16 | 0.01 | 0.41 | 7-16 |
| 029 Reforma - Bucareli | 29 / 33 | 0.00 | 0.37 | 25-33 |
| 118 Liverpool-Dinamarca | 3 / 19 | 0.33 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 13 / 15 | 0.00 | 0.32 | 9-15 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 450 (30/30) a 116 (0/23)
2. Llevar **10 bicis** de 555 (27/29) a 113 (0/15)
3. Llevar **10 bicis** de 098 (29/31) a 118 (3/19)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

572 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.034 |
| Sin resincronizar | 0.242 | 0.084 |
| Persistencia | 0.270 | 0.061 |
| Persistencia 0/1 | 0.270 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
