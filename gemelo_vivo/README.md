# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 13:51 (hora de Ciudad de México).

## Último pronóstico: 17/11 13:51 a 14:51

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.5 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 118 Liverpool-Dinamarca | 1 / 16 | 0.99 | 0.00 | 0-3 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-3 |
| 260 Av. Juárez-Balderas | 0 / 18 | 0.98 | 0.00 | 0-7 |
| 255 José Rosas Moreno-Guillermo  | 0 / 27 | 0.97 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 1 / 20 | 0.96 | 0.00 | 0-3 |
| 029 Reforma - Bucareli | 2 / 32 | 0.90 | 0.00 | 0-6 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 24 | 0.90 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 1 / 8 | 0.86 | 0.05 | 0-4 |
| 114 Lucerna-Abraham González | 2 / 20 | 0.83 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 3 / 31 | 0.80 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 117 (21/30) a 118 (1/16)
2. Llevar **6 bicis** de 116 (9/17) a 041 (1/20)
3. Llevar **4 bicis** de 085 (8/13) a 029 (2/32)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

43 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.151 | 0.031 |
| Sin resincronizar | 0.212 | 0.097 |
| Persistencia | 0.296 | 0.065 |
| Persistencia 0/1 | 0.296 | 0.065 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
