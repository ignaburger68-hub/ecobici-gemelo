# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 14:44 (hora de Ciudad de México).

## Último pronóstico: 19/11 14:44 a 15:44

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.8 °C** · sin lluvia · viento 8 km/h · día hábil

El clima multiplica los **retiros por 0.72** y las **devoluciones por 0.78** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 041 Reforma - Av. de la Repúblic | 0 / 24 | 0.99 | 0.00 | 0-6 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 0.99 | 0.00 | 0-7 |
| 270 De la República-Ponciano Arr | 0 / 24 | 0.99 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 0 / 27 | 0.98 | 0.00 | 0-7 |
| 255 José Rosas Moreno-Guillermo  | 0 / 31 | 0.98 | 0.00 | 0-6 |
| 029 Reforma - Bucareli | 0 / 31 | 0.96 | 0.00 | 1-10 |
| 048 Independencia - Azueta | 1 / 9 | 0.96 | 0.00 | 0-3 |
| 115 Roma-Dinamarca | 1 / 21 | 0.95 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 1 / 20 | 0.94 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 116 (16/16) a 555 (0/27)
2. Llevar **11 bicis** de 117 (19/26) a 115 (1/21)
3. Llevar **7 bicis** de 114 (14/17) a 256 (1/20)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

189 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.122 | 0.037 |
| Sin resincronizar | 0.285 | 0.094 |
| Persistencia | 0.331 | 0.071 |
| Persistencia 0/1 | 0.331 | 0.071 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
