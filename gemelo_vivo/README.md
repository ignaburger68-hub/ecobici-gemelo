# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 15:42 (hora de Ciudad de México).

## Último pronóstico: 18/11 15:42 a 16:42

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.4 °C** · sin lluvia · viento 9 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 1.00 | 0.00 | 0-4 |
| 026 Reforma - Versalles | 0 / 11 | 0.99 | 0.00 | 0-4 |
| 118 Liverpool-Dinamarca | 0 / 13 | 0.99 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 1 / 25 | 0.97 | 0.00 | 0-5 |
| 255 José Rosas Moreno-Guillermo  | 1 / 28 | 0.95 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 1 / 17 | 0.89 | 0.00 | 1-9 |
| 113 General Prim-Versalles | 1 / 11 | 0.81 | 0.00 | 0-5 |
| 020 Reforma- Río Támesis | 1 / 10 | 0.74 | 0.04 | 0-7 |
| 107-108 Tolsa-Balderas | 1 / 52 | 0.74 | 0.00 | 0-7 |
| 041 Reforma - Av. de la Repúblic | 2 / 24 | 0.66 | 0.00 | 0-7 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 031 (27/31) a 010 (1/25)
2. Llevar **8 bicis** de 117 (21/28) a 118 (0/13)
3. Llevar **6 bicis** de 012 (10/13) a 259 (0/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

122 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.126 | 0.032 |
| Sin resincronizar | 0.303 | 0.084 |
| Persistencia | 0.342 | 0.061 |
| Persistencia 0/1 | 0.342 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
