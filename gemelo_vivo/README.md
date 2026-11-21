# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 07:37 (hora de Ciudad de México).

## Último pronóstico: 21/11 07:37 a 08:37

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.2 °C** · sin lluvia · viento 2 km/h · día fin de semana

El clima multiplica los **retiros por 0.92** y las **devoluciones por 0.94** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 28 | 0.99 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 22 | 0.99 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 0 / 12 | 0.98 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 0 / 15 | 0.97 | 0.00 | 0-6 |
| 112 Av. Morelos-Abraham González | 1 / 19 | 0.70 | 0.00 | 0-5 |
| 114 Lucerna-Abraham González | 1 / 21 | 0.58 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 8 / 10 | 0.00 | 0.52 | 6-10 |
| 003 Reforma - Insurgentes | 3 / 28 | 0.13 | 0.00 | 1-5 |
| 085 Rosas Moreno - Sullivan | 3 / 15 | 0.10 | 0.00 | 1-7 |
| 086 Sullivan-Insurgentes | 5 / 15 | 0.06 | 0.01 | 2-10 |

### Plan recomendado del camión

1. Llevar **5 bicis** de 048 (8/10) a 119 (0/28)
2. Llevar **9 bicis** de 270 (15/26) a 020 (0/22)
3. Llevar **10 bicis** de 555 (21/30) a 112 (1/19)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

301 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
