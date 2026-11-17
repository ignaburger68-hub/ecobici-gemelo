# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 10:57 (hora de Ciudad de México).

## Último pronóstico: 17/11 10:57 a 11:57

![Mapa](ultimo/mapa.png)

### Clima de la hora y su efecto en la demanda

**17.1 °C** · sin lluvia · viento 1 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 270 De la República-Ponciano Arr | 0 / 25 | 0.99 | 0.00 | 0-4 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 0.99 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 7 | 0.98 | 0.01 | 0-3 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.98 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 10 / 10 | 0.01 | 0.98 | 5-10 |
| 026 Reforma - Versalles | 8 / 8 | 0.03 | 0.98 | 3-8 |
| 031 Hamburgo - Insurgentes | 0 / 29 | 0.97 | 0.00 | 0-6 |
| 555 Ribera de San Cosme - Insurg | 1 / 31 | 0.96 | 0.00 | 0-3 |
| 118 Liverpool-Dinamarca | 0 / 16 | 0.94 | 0.00 | 0-7 |
| 098 Emilio Dondé-Av. Balderas | 1 / 30 | 0.93 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **7 bicis** de 113 (10/10) a 555 (1/31)
2. Llevar **5 bicis** de 026 (8/8) a 098 (1/30)
3. Llevar **7 bicis** de 008 (15/16) a 270 (0/25)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

31 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.162 | 0.043 |
| Sin resincronizar | 0.186 | 0.085 |
| Persistencia | 0.305 | 0.094 |
| Persistencia 0/1 | 0.305 | 0.094 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
