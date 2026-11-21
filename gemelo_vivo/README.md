# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 08:19 (hora de Ciudad de México).

## Último pronóstico: 21/11 08:19 a 09:19

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
| 026 Reforma - Versalles | 0 / 12 | 0.99 | 0.00 | 0-6 |
| 112 Av. Morelos-Abraham González | 1 / 19 | 0.77 | 0.00 | 0-6 |
| 048 Independencia - Azueta | 10 / 11 | 0.00 | 0.70 | 7-11 |
| 116 Londres-Roma | 1 / 22 | 0.69 | 0.00 | 1-9 |
| 115 Roma-Dinamarca | 1 / 27 | 0.65 | 0.00 | 0-7 |
| 113 General Prim-Versalles | 1 / 15 | 0.57 | 0.00 | 0-6 |
| 119 Turín-Abraham González | 2 / 29 | 0.56 | 0.00 | 0-5 |
| 020 Reforma- Río Támesis | 3 / 22 | 0.39 | 0.00 | 1-9 |
| 114 Lucerna-Abraham González | 2 / 22 | 0.38 | 0.00 | 0-5 |
| 255 José Rosas Moreno-Guillermo  | 4 / 34 | 0.38 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **5 bicis** de 048 (10/11) a 026 (0/12)
2. Llevar **8 bicis** de 260 (14/19) a 112 (1/19)
3. Llevar **7 bicis** de 270 (16/26) a 116 (1/22)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

304 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
