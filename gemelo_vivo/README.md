# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 15:56 (hora de Ciudad de México).

## Último pronóstico: 18/11 15:56 a 16:56

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
| 031 Hamburgo - Insurgentes | 30 / 30 | 0.00 | 0.99 | 14-27 |
| 048 Independencia - Azueta | 0 / 8 | 0.99 | 0.05 | 0-6 |
| 010 Reforma - Ramírez | 0 / 25 | 0.98 | 0.00 | 0-5 |
| 116 Londres-Roma | 17 / 17 | 0.01 | 0.92 | 9-17 |
| 260 Av. Juárez-Balderas | 1 / 18 | 0.89 | 0.01 | 2-11 |
| 041 Reforma - Av. de la Repúblic | 1 / 24 | 0.88 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 1 / 11 | 0.87 | 0.00 | 0-4 |
| 450 Ramos Arizpe- Av México Teno | 1 / 26 | 0.82 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 2 / 26 | 0.81 | 0.00 | 0-8 |
| 259 Tómas Alva Edison-Ponciano A | 2 / 24 | 0.81 | 0.00 | 0-4 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 031 (30/30) a 010 (0/25)
2. Llevar **8 bicis** de 116 (17/17) a 555 (2/26)
3. Llevar **5 bicis** de 012 (10/13) a 041 (1/24)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

123 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.126 | 0.032 |
| Sin resincronizar | 0.303 | 0.084 |
| Persistencia | 0.343 | 0.062 |
| Persistencia 0/1 | 0.343 | 0.062 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
