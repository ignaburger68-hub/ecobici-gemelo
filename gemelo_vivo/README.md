# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 15:53 (hora de Ciudad de México).

## Último pronóstico: 22/11 15:53 a 16:53

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.9 °C** · lluvia 0.3 mm/h · viento 9 km/h · día fin de semana

El clima multiplica los **retiros por 0.66** y las **devoluciones por 0.71** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | llovió en las 3 h previas | 0.743 | 0.789 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 260 Av. Juárez-Balderas | 0 / 17 | 0.97 | 0.00 | 0-5 |
| 048 Independencia - Azueta | 11 / 11 | 0.01 | 0.96 | 6-11 |
| 115 Roma-Dinamarca | 1 / 25 | 0.80 | 0.00 | 0-5 |
| 085 Rosas Moreno - Sullivan | 1 / 14 | 0.74 | 0.00 | 0-5 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.64 | 0.00 | 0-5 |
| 029 Reforma - Bucareli | 30 / 32 | 0.00 | 0.63 | 27-32 |
| 026 Reforma - Versalles | 10 / 11 | 0.00 | 0.59 | 6-11 |
| 113 General Prim-Versalles | 2 / 15 | 0.57 | 0.00 | 0-5 |
| 270 De la República-Ponciano Arr | 22 / 26 | 0.00 | 0.42 | 18-26 |
| 119 Turín-Abraham González | 2 / 27 | 0.42 | 0.00 | 1-9 |

### Plan recomendado del camión

1. Llevar **9 bicis** de 029 (30/32) a 260 (0/17)
2. Llevar **5 bicis** de 048 (11/11) a 115 (1/25)
3. Llevar **7 bicis** de 270 (22/26) a 085 (1/14)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

407 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.034 |
| Sin resincronizar | 0.259 | 0.091 |
| Persistencia | 0.296 | 0.066 |
| Persistencia 0/1 | 0.296 | 0.066 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
