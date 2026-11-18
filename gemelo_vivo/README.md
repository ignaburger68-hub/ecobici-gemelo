# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 18/11/2026 10:28 (hora de Ciudad de México).

## Último pronóstico: 18/11 10:28 a 11:28

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**16.3 °C** · sin lluvia · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.81** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 115 Roma-Dinamarca | 21 / 21 | 0.00 | 0.99 | 19-21 |
| 107-108 Tolsa-Balderas | 0 / 54 | 0.99 | 0.00 | 0-4 |
| 263 Sadi Carnot - Gómez Farias | 0 / 29 | 0.99 | 0.00 | 0-4 |
| 255 José Rosas Moreno-Guillermo  | 0 / 32 | 0.99 | 0.00 | 0-5 |
| 117 Londres-Nápoles | 30 / 30 | 0.00 | 0.98 | 25-30 |
| 041 Reforma - Av. de la Repúblic | 0 / 23 | 0.97 | 0.00 | 0-6 |
| 031 Hamburgo - Insurgentes | 32 / 33 | 0.00 | 0.87 | 28-33 |
| 098 Emilio Dondé-Av. Balderas | 1 / 30 | 0.82 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 9 / 11 | 0.00 | 0.79 | 8-11 |
| 086 Sullivan-Insurgentes | 1 / 12 | 0.73 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 115 (21/21) a 107-108 (0/54)
2. Llevar **19 bicis** de 117 (30/30) a 098 (1/30)
3. Llevar **12 bicis** de 031 (32/33) a 041 (0/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

100 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.126 | 0.026 |
| Sin resincronizar | 0.312 | 0.084 |
| Persistencia | 0.357 | 0.047 |
| Persistencia 0/1 | 0.357 | 0.047 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
