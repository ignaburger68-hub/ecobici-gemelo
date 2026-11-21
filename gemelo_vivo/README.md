# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 06:54 (hora de Ciudad de México).

## Último pronóstico: 21/11 06:54 a 07:54

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**11.6 °C** · sin lluvia · viento 1 km/h · día fin de semana

El clima multiplica los **retiros por 0.92** y las **devoluciones por 0.94** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 114 Lucerna-Abraham González | 0 / 21 | 1.00 | 0.00 | 0-1 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.98 | 0.00 | 0-2 |
| 113 General Prim-Versalles | 0 / 15 | 0.98 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 22 | 0.98 | 0.00 | 0-2 |
| 119 Turín-Abraham González | 1 / 28 | 0.70 | 0.00 | 0-2 |
| 085 Rosas Moreno - Sullivan | 1 / 15 | 0.58 | 0.00 | 0-3 |
| 026 Reforma - Versalles | 1 / 12 | 0.30 | 0.00 | 0-3 |
| 031 Hamburgo - Insurgentes | 3 / 33 | 0.16 | 0.00 | 0-5 |
| 116 Londres-Roma | 4 / 22 | 0.11 | 0.00 | 1-6 |
| 118 Liverpool-Dinamarca | 3 / 17 | 0.03 | 0.00 | 2-5 |

### Plan recomendado del camión

1. Llevar **7 bicis** de 555 (19/30) a 114 (0/21)
2. Llevar **6 bicis** de 270 (15/27) a 020 (0/22)
3. Llevar **8 bicis** de 450 (24/29) a 112 (0/20)

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
