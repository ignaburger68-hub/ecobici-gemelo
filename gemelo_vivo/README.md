# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 07:36 (hora de Ciudad de México).

## Último pronóstico: 18/11 07:35 a 08:35

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**12.6 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.86** y las **devoluciones por 0.88** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 086 Sullivan-Insurgentes | 0 / 5 | 1.00 | 0.16 | 0-3 |
| 260 Av. Juárez-Balderas | 1 / 18 | 1.00 | 0.00 | 0-2 |
| 256 Gómez Farías-Sadi Carnot | 0 / 17 | 0.99 | 0.00 | 0-3 |
| 116 Londres-Roma | 0 / 17 | 0.97 | 0.05 | 3-14 |
| 010 Reforma - Ramírez | 3 / 27 | 0.96 | 0.00 | 1-9 |
| 026 Reforma - Versalles | 0 / 9 | 0.93 | 0.43 | 2-9 |
| 259 Tómas Alva Edison-Ponciano A | 4 / 24 | 0.88 | 0.00 | 0-1 |
| 555 Ribera de San Cosme - Insurg | 5 / 27 | 0.87 | 0.00 | 1-8 |
| 048 Independencia - Azueta | 1 / 7 | 0.82 | 0.01 | 0-4 |
| 119 Turín-Abraham González | 2 / 25 | 0.81 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 029 (16/31) a 260 (1/18)
2. Llevar **10 bicis** de 450 (24/27) a 010 (3/27)
3. Llevar **6 bicis** de 031 (9/33) a 256 (0/17)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

88 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.122 | 0.025 |
| Sin resincronizar | 0.316 | 0.091 |
| Persistencia | 0.349 | 0.045 |
| Persistencia 0/1 | 0.349 | 0.045 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
