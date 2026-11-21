# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 07:51 (hora de Ciudad de México).

## Último pronóstico: 21/11 07:51 a 08:51

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
| 020 Reforma- Río Támesis | 0 / 22 | 0.98 | 0.00 | 0-6 |
| 114 Lucerna-Abraham González | 0 / 21 | 0.97 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 0 / 12 | 0.94 | 0.00 | 0-6 |
| 113 General Prim-Versalles | 0 / 15 | 0.93 | 0.00 | 0-7 |
| 112 Av. Morelos-Abraham González | 1 / 19 | 0.68 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 8 / 10 | 0.00 | 0.58 | 6-10 |
| 255 José Rosas Moreno-Guillermo  | 3 / 33 | 0.34 | 0.00 | 0-4 |
| 003 Reforma - Insurgentes | 3 / 28 | 0.19 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 4 / 15 | 0.12 | 0.01 | 2-10 |

### Plan recomendado del camión

1. Llevar **4 bicis** de 048 (8/10) a 119 (0/28)
2. Llevar **7 bicis** de 260 (13/19) a 020 (0/22)
3. Llevar **6 bicis** de 270 (15/26) a 114 (0/21)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

302 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
