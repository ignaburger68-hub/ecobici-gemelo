# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 10:43 (hora de Ciudad de México).

## Último pronóstico: 17/11 10:43 a 11:43

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
| 255 José Rosas Moreno-Guillermo  | 0 / 28 | 0.99 | 0.00 | 0-2 |
| 256 Gómez Farías-Sadi Carnot | 0 / 20 | 0.99 | 0.00 | 0-3 |
| 086 Sullivan-Insurgentes | 0 / 7 | 0.98 | 0.03 | 0-4 |
| 112 Av. Morelos-Abraham González | 0 / 20 | 0.98 | 0.00 | 0-5 |
| 113 General Prim-Versalles | 10 / 10 | 0.01 | 0.96 | 5-10 |
| 031 Hamburgo - Insurgentes | 0 / 28 | 0.92 | 0.00 | 0-9 |
| 555 Ribera de San Cosme - Insurg | 1 / 31 | 0.92 | 0.00 | 0-4 |
| 270 De la República-Ponciano Arr | 1 / 25 | 0.91 | 0.00 | 0-5 |
| 098 Emilio Dondé-Av. Balderas | 1 / 30 | 0.82 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 1 / 10 | 0.82 | 0.01 | 0-5 |

### Plan recomendado del camión

1. Llevar **7 bicis** de 113 (10/10) a 555 (1/31)
2. Llevar **8 bicis** de 008 (14/16) a 256 (0/20)
3. Llevar **5 bicis** de 026 (7/9) a 255 (0/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

30 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.158 | 0.040 |
| Sin resincronizar | 0.179 | 0.082 |
| Persistencia | 0.308 | 0.094 |
| Persistencia 0/1 | 0.308 | 0.094 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
