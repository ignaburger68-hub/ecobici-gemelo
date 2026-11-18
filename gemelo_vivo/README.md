# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 06:53 (hora de Ciudad de México).

## Último pronóstico: 18/11 06:53 a 07:53

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.5 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 086 Sullivan-Insurgentes | 0 / 5 | 1.00 | 0.09 | 0-3 |
| 119 Turín-Abraham González | 0 / 25 | 1.00 | 0.00 | 0-3 |
| 114 Lucerna-Abraham González | 0 / 19 | 0.99 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 0 / 17 | 0.99 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 0 / 7 | 0.99 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 8 | 0.98 | 0.09 | 0-6 |
| 003 Reforma - Insurgentes | 0 / 31 | 0.98 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 0 / 23 | 0.97 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 1 / 18 | 0.95 | 0.00 | 0-1 |
| 450 Ramos Arizpe- Av México Teno | 27 / 27 | 0.00 | 0.94 | 16-25 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 450 (27/27) a 260 (1/18)
2. Llevar **10 bicis** de 010 (17/27) a 031 (1/23)
3. Llevar **4 bicis** de 118 (5/15) a 086 (0/5)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

85 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.122 | 0.025 |
| Sin resincronizar | 0.324 | 0.093 |
| Persistencia | 0.353 | 0.045 |
| Persistencia 0/1 | 0.353 | 0.045 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
