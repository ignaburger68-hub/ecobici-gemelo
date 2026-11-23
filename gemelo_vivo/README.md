# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 06:07 (hora de Ciudad de México).

## Último pronóstico: 23/11 06:06 a 07:06

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.3 °C** · sin lluvia · viento 0 km/h · día hábil

El clima multiplica los **retiros por 0.98** y las **devoluciones por 1.00** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más cálido (1 a 3 °C) | 1.019 | 1.036 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 048 Independencia - Azueta | 0 / 11 | 1.00 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 0 / 12 | 0.99 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 0 / 16 | 0.99 | 0.00 | 0-3 |
| 450 Ramos Arizpe- Av México Teno | 0 / 10 | 0.98 | 0.00 | 0-3 |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 0.98 | 0.27 | 1-5 |
| 020 Reforma- Río Támesis | 0 / 14 | 0.97 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 0 / 8 | 0.95 | 0.06 | 1-7 |
| 112 Av. Morelos-Abraham González | 1 / 20 | 0.55 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 1 / 26 | 0.43 | 0.00 | 0-4 |
| 260 Av. Juárez-Balderas | 18 / 19 | 0.01 | 0.38 | 10-18 |

### Plan recomendado del camión

1. Llevar **8 bicis** de 010 (10/25) a 086 (0/12)
2. Llevar **6 bicis** de 260 (18/19) a 048 (0/11)
3. Llevar **11 bicis** de 259 (17/26) a 555 (6/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

440 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.259 | 0.091 |
| Persistencia | 0.296 | 0.066 |
| Persistencia 0/1 | 0.296 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
