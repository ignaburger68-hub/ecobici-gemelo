# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 19/11/2026 14:01 (hora de Ciudad de México).

## Último pronóstico: 19/11 14:01 a 15:01

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.8 °C** · sin lluvia · viento 5 km/h · día hábil

El clima multiplica los **retiros por 0.72** y las **devoluciones por 0.78** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 119 Turín-Abraham González | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 270 De la República-Ponciano Arr | 0 / 25 | 0.99 | 0.00 | 0-5 |
| 086 Sullivan-Insurgentes | 0 / 16 | 0.99 | 0.00 | 0-6 |
| 256 Gómez Farías-Sadi Carnot | 0 / 19 | 0.99 | 0.00 | 0-3 |
| 555 Ribera de San Cosme - Insurg | 0 / 27 | 0.99 | 0.00 | 0-7 |
| 255 José Rosas Moreno-Guillermo  | 0 / 30 | 0.99 | 0.00 | 0-4 |
| 116 Londres-Roma | 16 / 16 | 0.00 | 0.99 | 9-16 |
| 029 Reforma - Bucareli | 0 / 30 | 0.98 | 0.00 | 0-7 |
| 260 Av. Juárez-Balderas | 0 / 19 | 0.97 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 0 / 14 | 0.97 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 116 (16/16) a 256 (0/19)
2. Llevar **8 bicis** de 114 (14/17) a 115 (1/21)
3. Llevar **6 bicis** de 118 (14/14) a 555 (0/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

186 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.122 | 0.037 |
| Sin resincronizar | 0.281 | 0.094 |
| Persistencia | 0.330 | 0.071 |
| Persistencia 0/1 | 0.330 | 0.071 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
