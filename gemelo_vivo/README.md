# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 16:25 (hora de Ciudad de México).

## Último pronóstico: 18/11 16:24 a 17:24

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.4 °C** · sin lluvia · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 118 Liverpool-Dinamarca | 0 / 12 | 0.99 | 0.01 | 0-6 |
| 010 Reforma - Ramírez | 0 / 25 | 0.99 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 0 / 11 | 0.99 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 0 / 18 | 0.98 | 0.00 | 0-7 |
| 048 Independencia - Azueta | 0 / 8 | 0.98 | 0.10 | 0-6 |
| 270 De la República-Ponciano Arr | 1 / 26 | 0.91 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 0 / 19 | 0.85 | 0.03 | 2-14 |
| 020 Reforma- Río Támesis | 1 / 10 | 0.84 | 0.01 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 2 / 24 | 0.77 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 2 / 24 | 0.64 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 031 (30/31) a 010 (0/25)
2. Llevar **7 bicis** de 115 (15/20) a 118 (0/12)
3. Llevar **6 bicis** de 116 (9/17) a 026 (0/11)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

125 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.126 | 0.032 |
| Sin resincronizar | 0.304 | 0.084 |
| Persistencia | 0.343 | 0.062 |
| Persistencia 0/1 | 0.343 | 0.062 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
