# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 14:20 (hora de Ciudad de México).

## Último pronóstico: 20/11 14:19 a 15:19

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**22.6 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.89** y las **devoluciones por 0.90** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 020 Reforma- Río Támesis | 0 / 21 | 0.99 | 0.00 | 0-3 |
| 116 Londres-Roma | 22 / 22 | 0.00 | 0.99 | 16-22 |
| 255 José Rosas Moreno-Guillermo  | 0 / 33 | 0.97 | 0.00 | 0-6 |
| 113 General Prim-Versalles | 15 / 15 | 0.01 | 0.95 | 5-14 |
| 118 Liverpool-Dinamarca | 19 / 19 | 0.00 | 0.94 | 10-18 |
| 117 Londres-Nápoles | 28 / 29 | 0.00 | 0.88 | 24-29 |
| 041 Reforma - Av. de la Repúblic | 1 / 29 | 0.85 | 0.00 | 0-6 |
| 010 Reforma - Ramírez | 1 / 25 | 0.84 | 0.00 | 0-6 |
| 031 Hamburgo - Insurgentes | 32 / 34 | 0.00 | 0.75 | 23-33 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 116 (22/22) a 020 (0/21)
2. Llevar **16 bicis** de 117 (28/29) a 041 (1/29)
3. Llevar **13 bicis** de 031 (32/34) a 010 (1/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

258 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.118 | 0.034 |
| Sin resincronizar | 0.273 | 0.091 |
| Persistencia | 0.311 | 0.066 |
| Persistencia 0/1 | 0.311 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
