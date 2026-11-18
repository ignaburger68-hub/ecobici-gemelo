# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 14:17 (hora de Ciudad de México).

## Último pronóstico: 18/11 14:17 a 15:17

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.9 °C** · sin lluvia · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 041 Reforma - Av. de la Repúblic | 0 / 23 | 0.99 | 0.00 | 0-7 |
| 048 Independencia - Azueta | 0 / 9 | 0.97 | 0.02 | 0-4 |
| 020 Reforma- Río Támesis | 1 / 11 | 0.85 | 0.00 | 0-4 |
| 031 Hamburgo - Insurgentes | 31 / 33 | 0.00 | 0.76 | 25-33 |
| 117 Londres-Nápoles | 28 / 30 | 0.00 | 0.76 | 24-30 |
| 260 Av. Juárez-Balderas | 1 / 19 | 0.75 | 0.00 | 0-8 |
| 118 Liverpool-Dinamarca | 2 / 13 | 0.70 | 0.01 | 0-6 |
| 107-108 Tolsa-Balderas | 2 / 52 | 0.65 | 0.00 | 0-7 |
| 010 Reforma - Ramírez | 2 / 25 | 0.65 | 0.00 | 0-7 |
| 026 Reforma - Versalles | 8 / 11 | 0.01 | 0.51 | 4-11 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 031 (31/33) a 041 (0/23)
2. Llevar **13 bicis** de 117 (28/30) a 010 (2/25)
3. Llevar **5 bicis** de 116 (10/16) a 048 (0/9)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

116 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.124 | 0.029 |
| Sin resincronizar | 0.305 | 0.083 |
| Persistencia | 0.342 | 0.057 |
| Persistencia 0/1 | 0.342 | 0.057 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
