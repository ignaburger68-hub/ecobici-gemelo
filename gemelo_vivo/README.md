# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 12:08 (hora de Ciudad de México).

## Último pronóstico: 20/11 12:08 a 13:08

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.4 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 117 Londres-Nápoles | 30 / 30 | 0.00 | 1.00 | 27-30 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 1.00 | 11-15 |
| 116 Londres-Roma | 22 / 22 | 0.00 | 1.00 | 18-22 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 0.99 | 17-20 |
| 256 Gómez Farías-Sadi Carnot | 0 / 23 | 0.99 | 0.00 | 0-2 |
| 255 José Rosas Moreno-Guillermo  | 0 / 33 | 0.98 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 0 / 32 | 0.98 | 0.00 | 0-5 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 26 | 0.97 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 0 / 25 | 0.94 | 0.00 | 0-8 |

### Plan recomendado del camión

1. Llevar **19 bicis** de 117 (30/30) a 555 (0/32)
2. Llevar **15 bicis** de 116 (22/22) a 256 (0/23)
3. Llevar **14 bicis** de 260 (20/20) a 255 (0/33)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

249 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.119 | 0.034 |
| Sin resincronizar | 0.277 | 0.091 |
| Persistencia | 0.316 | 0.065 |
| Persistencia 0/1 | 0.316 | 0.065 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
