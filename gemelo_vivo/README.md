# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 07:03 (hora de Ciudad de México).

## Último pronóstico: 23/11 07:03 a 08:03

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.9 °C** · sin lluvia · viento 1 km/h · día hábil

El clima multiplica los **retiros por 0.98** y las **devoluciones por 1.00** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más cálido (1 a 3 °C) | 1.019 | 1.036 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 086 Sullivan-Insurgentes | 0 / 12 | 1.00 | 0.00 | 0-2 |
| 555 Ribera de San Cosme - Insurg | 1 / 30 | 1.00 | 0.00 | 0-2 |
| 048 Independencia - Azueta | 0 / 11 | 0.99 | 0.00 | 0-2 |
| 450 Ramos Arizpe- Av México Teno | 0 / 10 | 0.97 | 0.00 | 0-4 |
| 008 Reforma - General Prim | 0 / 14 | 0.95 | 0.00 | 1-6 |
| 020 Reforma- Río Támesis | 0 / 14 | 0.94 | 0.04 | 3-11 |
| 118 Liverpool-Dinamarca | 13 / 16 | 0.00 | 0.92 | 10-16 |
| 026 Reforma - Versalles | 0 / 8 | 0.91 | 0.25 | 2-8 |
| 119 Turín-Abraham González | 1 / 26 | 0.85 | 0.00 | 0-3 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 118 (13/16) a 555 (1/30)
2. Llevar **10 bicis** de 098 (15/26) a 086 (0/12)
3. Llevar **7 bicis** de 259 (15/26) a 116 (1/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

441 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.259 | 0.091 |
| Persistencia | 0.295 | 0.066 |
| Persistencia 0/1 | 0.295 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
