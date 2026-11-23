# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 07:46 (hora de Ciudad de México).

## Último pronóstico: 23/11 07:46 a 08:46

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.6 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 1.00 | 0.00 | 0-2 |
| 003 Reforma - Insurgentes | 0 / 26 | 0.99 | 0.00 | 0-3 |
| 450 Ramos Arizpe- Av México Teno | 0 / 11 | 0.97 | 0.00 | 1-5 |
| 086 Sullivan-Insurgentes | 2 / 12 | 0.96 | 0.00 | 0-3 |
| 041 Reforma - Av. de la Repúblic | 1 / 26 | 0.95 | 0.00 | 0-6 |
| 008 Reforma - General Prim | 0 / 14 | 0.90 | 0.02 | 2-10 |
| 263 Sadi Carnot - Gómez Farias | 3 / 27 | 0.88 | 0.00 | 0-2 |
| 026 Reforma - Versalles | 0 / 8 | 0.85 | 0.73 | 5-8 |
| 020 Reforma- Río Támesis | 0 / 15 | 0.82 | 0.36 | 7-15 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 098 (15/26) a 555 (0/31)
2. Llevar **7 bicis** de 115 (7/25) a 086 (2/12)
3. Llevar **7 bicis** de 029 (12/33) a 041 (1/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

444 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.034 |
| Sin resincronizar | 0.256 | 0.090 |
| Persistencia | 0.293 | 0.065 |
| Persistencia 0/1 | 0.293 | 0.065 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
