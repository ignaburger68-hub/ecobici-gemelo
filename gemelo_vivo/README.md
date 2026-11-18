# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 08:48 (hora de Ciudad de México).

## Último pronóstico: 18/11 08:48 a 09:48

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.3 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 270 De la República-Ponciano Arr | 0 / 22 | 1.00 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 0 / 28 | 1.00 | 0.00 | 0-7 |
| 263 Sadi Carnot - Gómez Farias | 0 / 27 | 1.00 | 0.00 | 0-1 |
| 107-108 Tolsa-Balderas | 2 / 53 | 0.99 | 0.00 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 31 | 0.99 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 0 / 9 | 0.99 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 0 / 18 | 0.99 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 1 / 29 | 0.99 | 0.00 | 0-1 |
| 113 General Prim-Versalles | 9 / 10 | 0.02 | 0.98 | 3-10 |
| 026 Reforma - Versalles | 10 / 10 | 0.10 | 0.97 | 2-10 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 113 (9/10) a 270 (0/22)
2. Llevar **8 bicis** de 026 (10/10) a 555 (0/28)
3. Llevar **13 bicis** de 031 (17/31) a 107-108 (2/53)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

93 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.127 | 0.025 |
| Sin resincronizar | 0.317 | 0.088 |
| Persistencia | 0.358 | 0.043 |
| Persistencia 0/1 | 0.358 | 0.043 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
