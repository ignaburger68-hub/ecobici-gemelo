# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 07:38 (hora de Ciudad de México).

## Último pronóstico: 17/11 07:38 a 08:38

![Mapa](ultimo/mapa.png)

### Clima de la hora y su efecto en la demanda

**12.7 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.86** y las **devoluciones por 0.88** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 1.00 | 0.00 | 0-1 |
| 450 Ramos Arizpe- Av México Teno | 1 / 28 | 1.00 | 0.00 | 0-1 |
| 107-108 Tolsa-Balderas | 0 / 53 | 1.00 | 0.00 | 0-2 |
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 1.00 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 0 / 7 | 1.00 | 0.03 | 0-3 |
| 003 Reforma - Insurgentes | 0 / 31 | 0.99 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 1 / 28 | 0.98 | 0.00 | 0-2 |
| 118 Liverpool-Dinamarca | 16 / 16 | 0.00 | 0.97 | 12-16 |
| 026 Reforma - Versalles | 9 / 10 | 0.00 | 0.97 | 7-10 |
| 113 General Prim-Versalles | 8 / 10 | 0.00 | 0.96 | 8-10 |

### Plan recomendado del camión

1. Llevar **17 bicis** de 116 (17/18) a 107-108 (0/53)
2. Llevar **14 bicis** de 118 (16/16) a 450 (1/28)
3. Llevar **9 bicis** de 026 (9/10) a 555 (0/31)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

17 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.056 | 0.064 |
| Sin resincronizar | 0.121 | 0.072 |
| Persistencia | 0.222 | 0.148 |
| Persistencia 0/1 | 0.222 | 0.148 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
