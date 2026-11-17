# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 12:54 (hora de Ciudad de México).

## Último pronóstico: 17/11 12:54 a 13:54

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.1 °C** · sin lluvia · viento 3 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 020 Reforma- Río Támesis | 0 / 9 | 1.00 | 0.01 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 0 / 20 | 1.00 | 0.00 | 0-5 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 0.99 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 1 / 27 | 0.88 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 3 / 31 | 0.85 | 0.00 | 0-5 |
| 029 Reforma - Bucareli | 2 / 32 | 0.83 | 0.00 | 0-5 |
| 263 Sadi Carnot - Gómez Farias | 1 / 29 | 0.81 | 0.00 | 0-3 |
| 450 Ramos Arizpe- Av México Teno | 1 / 28 | 0.79 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 2 / 7 | 0.67 | 0.15 | 0-5 |
| 113 General Prim-Versalles | 2 / 10 | 0.62 | 0.03 | 0-6 |

### Plan recomendado del camión

1. Llevar **13 bicis** de 117 (23/30) a 041 (0/20)
2. Llevar **6 bicis** de 085 (11/14) a 555 (3/31)
3. Llevar **6 bicis** de 008 (11/15) a 256 (0/19)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

39 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.150 | 0.034 |
| Sin resincronizar | 0.203 | 0.101 |
| Persistencia | 0.292 | 0.077 |
| Persistencia 0/1 | 0.292 | 0.077 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
