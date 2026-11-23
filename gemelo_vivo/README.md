# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 16:54 (hora de Ciudad de México).

## Último pronóstico: 23/11 16:54 a 17:54

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.8 °C** · sin lluvia · viento 7 km/h · día hábil

El clima multiplica los **retiros por 0.71** y las **devoluciones por 0.77** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 010 Reforma - Ramírez | 0 / 26 | 0.99 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 0 / 18 | 0.97 | 0.00 | 0-7 |
| 020 Reforma- Río Támesis | 1 / 19 | 0.89 | 0.00 | 0-4 |
| 012 Río Lerma - Villalongín | 1 / 14 | 0.88 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 1 / 26 | 0.84 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 1 / 11 | 0.84 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 1 / 27 | 0.74 | 0.00 | 0-6 |
| 112 Av. Morelos-Abraham González | 2 / 19 | 0.71 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 3 / 26 | 0.53 | 0.00 | 3-15 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 029 (26/34) a 010 (0/26)
2. Llevar **6 bicis** de 260 (9/20) a 020 (1/19)
3. Llevar **10 bicis** de 031 (26/35) a 003 (1/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

482 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.031 |
| Sin resincronizar | 0.254 | 0.087 |
| Persistencia | 0.289 | 0.060 |
| Persistencia 0/1 | 0.289 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
