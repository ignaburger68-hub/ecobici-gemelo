# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 07:23 (hora de Ciudad de México).

## Último pronóstico: 21/11 07:23 a 08:23

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.3 °C** · sin lluvia · viento 1 km/h · día fin de semana

El clima multiplica los **retiros por 0.92** y las **devoluciones por 0.94** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 28 | 0.99 | 0.00 | 0-2 |
| 020 Reforma- Río Támesis | 0 / 22 | 0.99 | 0.00 | 0-4 |
| 112 Av. Morelos-Abraham González | 1 / 20 | 0.70 | 0.00 | 0-4 |
| 114 Lucerna-Abraham González | 1 / 21 | 0.64 | 0.00 | 0-3 |
| 085 Rosas Moreno - Sullivan | 1 / 15 | 0.53 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 1 / 15 | 0.41 | 0.00 | 1-6 |
| 026 Reforma - Versalles | 1 / 13 | 0.36 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 8 / 11 | 0.00 | 0.22 | 6-11 |
| 031 Hamburgo - Insurgentes | 2 / 33 | 0.22 | 0.00 | 1-7 |
| 003 Reforma - Insurgentes | 3 / 28 | 0.07 | 0.00 | 1-4 |

### Plan recomendado del camión

1. Llevar **5 bicis** de 048 (8/11) a 119 (0/28)
2. Llevar **10 bicis** de 450 (24/29) a 020 (0/22)
3. Llevar **10 bicis** de 098 (20/31) a 112 (1/20)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

300 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
