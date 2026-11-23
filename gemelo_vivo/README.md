# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 10:58 (hora de Ciudad de México).

## Último pronóstico: 23/11 10:58 a 11:58

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
| 008 Reforma - General Prim | 0 / 15 | 0.99 | 0.00 | 0-2 |
| 026 Reforma - Versalles | 14 / 14 | 0.00 | 0.98 | 9-14 |
| 118 Liverpool-Dinamarca | 18 / 18 | 0.00 | 0.97 | 14-18 |
| 048 Independencia - Azueta | 0 / 11 | 0.97 | 0.01 | 0-6 |
| 255 José Rosas Moreno-Guillermo  | 1 / 34 | 0.83 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 1 / 15 | 0.79 | 0.00 | 0-5 |
| 003 Reforma - Insurgentes | 1 / 28 | 0.68 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 1 / 20 | 0.63 | 0.00 | 1-9 |
| 107-108 Tolsa-Balderas | 3 / 57 | 0.62 | 0.00 | 1-10 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 118 (18/18) a 008 (0/15)
2. Llevar **6 bicis** de 026 (14/14) a 048 (0/11)
3. Llevar **12 bicis** de 115 (23/26) a 255 (1/34)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

457 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.117 | 0.033 |
| Sin resincronizar | 0.255 | 0.088 |
| Persistencia | 0.294 | 0.064 |
| Persistencia 0/1 | 0.294 | 0.064 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
