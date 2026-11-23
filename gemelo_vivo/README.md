# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 10:30 (hora de Ciudad de México).

## Último pronóstico: 23/11 10:30 a 11:30

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.3 °C** · sin lluvia · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 118 Liverpool-Dinamarca | 18 / 18 | 0.00 | 0.99 | 14-18 |
| 048 Independencia - Azueta | 0 / 11 | 0.98 | 0.00 | 0-5 |
| 041 Reforma - Av. de la Repúblic | 1 / 31 | 0.86 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 3 / 32 | 0.78 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 2 / 15 | 0.73 | 0.00 | 0-5 |
| 119 Turín-Abraham González | 1 / 29 | 0.73 | 0.00 | 0-8 |
| 255 José Rosas Moreno-Guillermo  | 2 / 34 | 0.68 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 11 / 13 | 0.00 | 0.64 | 7-13 |
| 107-108 Tolsa-Balderas | 4 / 58 | 0.57 | 0.00 | 0-6 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 118 (18/18) a 555 (3/32)
2. Llevar **6 bicis** de 026 (11/13) a 048 (0/11)
3. Llevar **13 bicis** de 115 (23/26) a 041 (1/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

455 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.116 | 0.033 |
| Sin resincronizar | 0.256 | 0.088 |
| Persistencia | 0.295 | 0.064 |
| Persistencia 0/1 | 0.295 | 0.064 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
