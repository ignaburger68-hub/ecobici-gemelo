# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 09:46 (hora de Ciudad de México).

## Último pronóstico: 17/11 09:46 a 10:46

![Mapa](ultimo/mapa.png)

### Clima de la hora y su efecto en la demanda

**15.7 °C** · sin lluvia · viento 1 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 1.00 | 0.00 | 0-2 |
| 048 Independencia - Azueta | 0 / 9 | 1.00 | 0.00 | 0-2 |
| 086 Sullivan-Insurgentes | 0 / 7 | 1.00 | 0.00 | 0-2 |
| 259 Tómas Alva Edison-Ponciano A | 0 / 24 | 0.99 | 0.00 | 0-3 |
| 119 Turín-Abraham González | 0 / 25 | 0.99 | 0.00 | 0-5 |
| 085 Rosas Moreno - Sullivan | 0 / 14 | 0.99 | 0.00 | 0-3 |
| 260 Av. Juárez-Balderas | 0 / 20 | 0.99 | 0.00 | 0-3 |
| 255 José Rosas Moreno-Guillermo  | 0 / 28 | 0.99 | 0.00 | 0-3 |
| 008 Reforma - General Prim | 16 / 16 | 0.00 | 0.98 | 11-16 |
| 113 General Prim-Versalles | 0 / 10 | 0.97 | 0.01 | 0-5 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 008 (16/16) a 119 (0/25)
2. Llevar **7 bicis** de 555 (17/31) a 048 (0/9)
3. Llevar **9 bicis** de 107-108 (17/53) a 260 (0/20)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

26 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.139 | 0.045 |
| Sin resincronizar | 0.148 | 0.074 |
| Persistencia | 0.337 | 0.103 |
| Persistencia 0/1 | 0.337 | 0.103 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
