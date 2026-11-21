# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 06:26 (hora de Ciudad de México).

## Último pronóstico: 21/11 06:26 a 07:26

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**10.3 °C** · sin lluvia · viento 1 km/h · día fin de semana

El clima multiplica los **retiros por 0.92** y las **devoluciones por 0.94** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 28 | 1.00 | 0.00 | 0-2 |
| 113 General Prim-Versalles | 0 / 15 | 0.99 | 0.00 | 0-3 |
| 085 Rosas Moreno - Sullivan | 0 / 15 | 0.99 | 0.00 | 0-2 |
| 010 Reforma - Ramírez | 0 / 25 | 0.98 | 0.00 | 0-5 |
| 020 Reforma- Río Támesis | 1 / 22 | 0.67 | 0.00 | 0-3 |
| 114 Lucerna-Abraham González | 1 / 21 | 0.59 | 0.00 | 0-2 |
| 031 Hamburgo - Insurgentes | 2 / 33 | 0.45 | 0.00 | 0-3 |
| 112 Av. Morelos-Abraham González | 1 / 20 | 0.43 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 1 / 26 | 0.34 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 1 / 12 | 0.26 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **6 bicis** de 450 (23/28) a 085 (0/15)
2. Llevar **7 bicis** de 450 (23/28) a 119 (0/28)
3. Llevar **5 bicis** de 270 (13/27) a 020 (1/22)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

298 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
