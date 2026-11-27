# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 27/11/2026 06:19 (hora de Ciudad de México).

## Último pronóstico: 27/11 06:18 a 07:18

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**9.4 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 6 | 1.00 | 0.00 | 0-0 |
| 041 Reforma - Av. de la Repúblic | 0 / 25 | 1.00 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 0 / 24 | 0.99 | 0.00 | 0-2 |
| 031 Hamburgo - Insurgentes | 0 / 34 | 0.99 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 0 / 9 | 0.97 | 0.03 | 1-6 |
| 107-108 Tolsa-Balderas | 0 / 16 | 0.93 | 0.00 | 2-9 |
| 020 Reforma- Río Támesis | 1 / 21 | 0.74 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 1 / 11 | 0.54 | 0.00 | 0-3 |
| 085 Rosas Moreno - Sullivan | 8 / 10 | 0.01 | 0.45 | 5-10 |
| 117 Londres-Nápoles | 2 / 28 | 0.29 | 0.00 | 1-7 |

### Plan recomendado del camión

1. Llevar **4 bicis** de 085 (8/10) a 041 (0/25)
2. Llevar **5 bicis** de 256 (18/21) a 031 (0/34)
3. Llevar **9 bicis** de 450 (20/23) a 020 (1/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

725 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.036 |
| Sin resincronizar | 0.247 | 0.081 |
| Persistencia | 0.255 | 0.061 |
| Persistencia 0/1 | 0.255 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
