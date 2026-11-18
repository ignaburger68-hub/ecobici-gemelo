# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 15:28 (hora de Ciudad de México).

## Último pronóstico: 18/11 15:28 a 16:28

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.1 °C** · sin lluvia · viento 8 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.99 | 0.00 | 0-5 |
| 020 Reforma- Río Támesis | 0 / 10 | 0.98 | 0.01 | 0-6 |
| 555 Ribera de San Cosme - Insurg | 0 / 27 | 0.96 | 0.00 | 1-9 |
| 118 Liverpool-Dinamarca | 1 / 13 | 0.94 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 2 / 25 | 0.91 | 0.00 | 0-6 |
| 048 Independencia - Azueta | 1 / 8 | 0.90 | 0.03 | 0-5 |
| 113 General Prim-Versalles | 1 / 10 | 0.80 | 0.01 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 1 / 24 | 0.77 | 0.00 | 0-7 |
| 107-108 Tolsa-Balderas | 1 / 52 | 0.73 | 0.00 | 0-8 |
| 031 Hamburgo - Insurgentes | 29 / 31 | 0.00 | 0.73 | 22-30 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 031 (29/31) a 010 (2/25)
2. Llevar **9 bicis** de 117 (27/29) a 118 (1/13)
3. Llevar **6 bicis** de 031 (29/31) a 555 (0/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

121 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.125 | 0.032 |
| Sin resincronizar | 0.303 | 0.084 |
| Persistencia | 0.341 | 0.061 |
| Persistencia 0/1 | 0.341 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
