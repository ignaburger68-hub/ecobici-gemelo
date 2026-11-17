# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 07:24 (hora de Ciudad de México).

## Último pronóstico: 17/11 07:24 a 08:24

![Mapa](ultimo/mapa.png)

### Clima de la hora y su efecto en la demanda

**11.3 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.89** y las **devoluciones por 0.90** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 1.00 | 0.00 | 0-1 |
| 555 Ribera de San Cosme - Insurg | 0 / 31 | 1.00 | 0.00 | 0-3 |
| 118 Liverpool-Dinamarca | 16 / 16 | 0.00 | 1.00 | 13-16 |
| 107-108 Tolsa-Balderas | 1 / 53 | 1.00 | 0.00 | 0-1 |
| 086 Sullivan-Insurgentes | 0 / 7 | 0.99 | 0.05 | 0-3 |
| 012 Río Lerma - Villalongín | 15 / 15 | 0.00 | 0.99 | 8-15 |
| 255 José Rosas Moreno-Guillermo  | 2 / 28 | 0.98 | 0.00 | 0-3 |
| 113 General Prim-Versalles | 9 / 10 | 0.00 | 0.97 | 9-10 |
| 026 Reforma - Versalles | 8 / 10 | 0.00 | 0.95 | 8-10 |
| 450 Ramos Arizpe- Av México Teno | 6 / 28 | 0.94 | 0.00 | 0-1 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 118 (16/16) a 107-108 (1/53)
2. Llevar **15 bicis** de 116 (17/18) a 555 (0/31)
3. Llevar **9 bicis** de 113 (9/10) a 263 (0/29)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

16 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.076 | 0.082 |
| Sin resincronizar | 0.139 | 0.080 |
| Persistencia | 0.226 | 0.151 |
| Persistencia 0/1 | 0.226 | 0.151 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
