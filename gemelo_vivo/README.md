# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 20/11/2026 11:54 (hora de Ciudad de México).

## Último pronóstico: 20/11 11:54 a 12:54

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
| 255 José Rosas Moreno-Guillermo  | 0 / 33 | 0.99 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 0 / 32 | 0.99 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 0 / 23 | 0.99 | 0.00 | 0-3 |
| 260 Av. Juárez-Balderas | 20 / 20 | 0.00 | 0.98 | 16-20 |
| 113 General Prim-Versalles | 15 / 15 | 0.00 | 0.98 | 11-15 |
| 048 Independencia - Azueta | 10 / 10 | 0.01 | 0.97 | 4-10 |
| 116 Londres-Roma | 20 / 22 | 0.00 | 0.78 | 17-22 |
| 026 Reforma - Versalles | 11 / 12 | 0.00 | 0.71 | 6-12 |
| 041 Reforma - Av. de la Repúblic | 2 / 29 | 0.71 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 260 (20/20) a 555 (0/32)
2. Llevar **10 bicis** de 113 (15/15) a 255 (0/33)
3. Llevar **12 bicis** de 116 (20/22) a 256 (0/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

248 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.119 | 0.034 |
| Sin resincronizar | 0.277 | 0.091 |
| Persistencia | 0.316 | 0.064 |
| Persistencia 0/1 | 0.316 | 0.064 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
