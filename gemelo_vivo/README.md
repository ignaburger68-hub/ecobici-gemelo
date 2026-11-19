# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 20:52 (hora de Ciudad de México).

## Último pronóstico: 18/11 20:52 a 21:52

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.8 °C** · sin lluvia · viento 8 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 117 Londres-Nápoles | 0 / 28 | 1.00 | 0.00 | 0-3 |
| 118 Liverpool-Dinamarca | 0 / 12 | 0.99 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 10 | 0.99 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 0 / 9 | 0.99 | 0.05 | 0-6 |
| 115 Roma-Dinamarca | 0 / 21 | 0.99 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 18 / 18 | 0.00 | 0.99 | 12-18 |
| 008 Reforma - General Prim | 0 / 13 | 0.98 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 9 / 9 | 0.17 | 0.96 | 1-8 |
| 041 Reforma - Av. de la Repúblic | 1 / 23 | 0.92 | 0.00 | 0-6 |
| 116 Londres-Roma | 1 / 17 | 0.82 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 260 (18/18) a 020 (0/10)
2. Llevar **13 bicis** de 450 (18/24) a 041 (1/23)
3. Llevar **5 bicis** de 026 (9/9) a 086 (0/9)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

143 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.127 | 0.034 |
| Sin resincronizar | 0.303 | 0.087 |
| Persistencia | 0.344 | 0.068 |
| Persistencia 0/1 | 0.344 | 0.068 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
