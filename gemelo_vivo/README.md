# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 11:12 (hora de Ciudad de México).

## Último pronóstico: 21/11 11:12 a 12:12

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.6 °C** · sin lluvia · viento 4 km/h · día fin de semana

El clima multiplica los **retiros por 0.92** y las **devoluciones por 0.94** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 118 Liverpool-Dinamarca | 0 / 18 | 0.99 | 0.00 | 0-3 |
| 085 Rosas Moreno - Sullivan | 1 / 15 | 0.80 | 0.00 | 0-3 |
| 119 Turín-Abraham González | 1 / 29 | 0.76 | 0.00 | 0-4 |
| 116 Londres-Roma | 2 / 23 | 0.68 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 27 / 30 | 0.00 | 0.64 | 23-30 |
| 020 Reforma- Río Támesis | 3 / 23 | 0.57 | 0.00 | 0-8 |
| 112 Av. Morelos-Abraham González | 2 / 22 | 0.56 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 2 / 17 | 0.55 | 0.00 | 0-6 |
| 255 José Rosas Moreno-Guillermo  | 3 / 32 | 0.43 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 3 / 26 | 0.39 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 270 (27/30) a 118 (0/18)
2. Llevar **8 bicis** de 450 (28/30) a 085 (1/15)
3. Llevar **6 bicis** de 260 (13/21) a 116 (2/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

316 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
