# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 06:13 (hora de Ciudad de México).

## Último pronóstico: 17/11 06:13 a 07:13

![Mapa](ultimo/mapa.png)

### Clima de la hora y su efecto en la demanda

**11.1 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 14 | 0.99 | 0.00 | 0-4 |
| 098 Emilio Dondé-Av. Balderas | 0 / 19 | 0.99 | 0.00 | 0-2 |
| 114 Lucerna-Abraham González | 20 / 20 | 0.00 | 0.99 | 15-20 |
| 086 Sullivan-Insurgentes | 0 / 7 | 0.98 | 0.11 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 0 / 17 | 0.95 | 0.00 | 2-9 |
| 555 Ribera de San Cosme - Insurg | 1 / 31 | 0.93 | 0.00 | 0-3 |
| 107-108 Tolsa-Balderas | 3 / 53 | 0.89 | 0.00 | 0-2 |
| 255 José Rosas Moreno-Guillermo  | 2 / 28 | 0.77 | 0.00 | 0-2 |
| 119 Turín-Abraham González | 2 / 25 | 0.66 | 0.00 | 0-3 |
| 020 Reforma- Río Támesis | 1 / 12 | 0.59 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 010 (12/27) a 555 (1/31)
2. Llevar **10 bicis** de 118 (11/16) a 107-108 (3/53)
3. Llevar **9 bicis** de 012 (13/15) a 255 (2/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

14 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | nan | nan |
| Sin resincronizar | nan | nan |
| Persistencia | nan | nan |
| Persistencia 0/1 | nan | nan |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
