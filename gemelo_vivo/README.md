# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 12:26 (hora de Ciudad de México).

## Último pronóstico: 17/11 12:25 a 13:25

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**18.6 °C** · sin lluvia · viento 1 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 048 Independencia - Azueta | 0 / 10 | 0.99 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 0 / 7 | 0.99 | 0.09 | 0-5 |
| 020 Reforma- Río Támesis | 1 / 9 | 0.89 | 0.01 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 1 / 20 | 0.85 | 0.00 | 0-3 |
| 263 Sadi Carnot - Gómez Farias | 1 / 29 | 0.84 | 0.00 | 0-2 |
| 256 Gómez Farías-Sadi Carnot | 2 / 19 | 0.79 | 0.00 | 0-3 |
| 450 Ramos Arizpe- Av México Teno | 1 / 28 | 0.77 | 0.00 | 0-4 |
| 555 Ribera de San Cosme - Insurg | 3 / 30 | 0.75 | 0.00 | 0-6 |
| 113 General Prim-Versalles | 1 / 10 | 0.74 | 0.01 | 0-6 |
| 259 Tómas Alva Edison-Ponciano A | 1 / 24 | 0.72 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **6 bicis** de 117 (23/30) a 086 (0/7)
2. Llevar **10 bicis** de 117 (23/30) a 041 (1/20)
3. Llevar **5 bicis** de 008 (12/15) a 048 (0/10)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

37 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.154 | 0.036 |
| Sin resincronizar | 0.204 | 0.098 |
| Persistencia | 0.293 | 0.084 |
| Persistencia 0/1 | 0.293 | 0.084 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
