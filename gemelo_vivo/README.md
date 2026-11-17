# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 11:57 (hora de Ciudad de México).

## Último pronóstico: 17/11 11:57 a 12:57

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.6 °C** · sin lluvia · viento 1 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 086 Sullivan-Insurgentes | 0 / 7 | 0.99 | 0.05 | 0-4 |
| 008 Reforma - General Prim | 16 / 16 | 0.00 | 0.99 | 10-16 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.98 | 0.00 | 0-3 |
| 048 Independencia - Azueta | 0 / 10 | 0.97 | 0.01 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 0 / 20 | 0.97 | 0.00 | 0-5 |
| 012 Río Lerma - Villalongín | 1 / 15 | 0.69 | 0.00 | 0-6 |
| 114 Lucerna-Abraham González | 1 / 20 | 0.65 | 0.00 | 1-8 |
| 450 Ramos Arizpe- Av México Teno | 1 / 28 | 0.57 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 7 / 9 | 0.04 | 0.53 | 2-9 |
| 113 General Prim-Versalles | 2 / 10 | 0.52 | 0.06 | 0-8 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 008 (16/16) a 041 (0/20)
2. Llevar **4 bicis** de 085 (10/14) a 086 (0/7)
3. Llevar **4 bicis** de 026 (7/9) a 048 (0/10)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

35 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.155 | 0.038 |
| Sin resincronizar | 0.202 | 0.095 |
| Persistencia | 0.300 | 0.088 |
| Persistencia 0/1 | 0.300 | 0.088 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
