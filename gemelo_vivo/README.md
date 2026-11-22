# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 22/11/2026 12:21 (hora de Ciudad de México).

## Último pronóstico: 22/11 12:21 a 13:21

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.9 °C** · lluvia 0.1 mm/h · viento 2 km/h · día fin de semana

El clima multiplica los **retiros por 0.88** y las **devoluciones por 0.89** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.901 | 0.896 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 008 Reforma - General Prim | 0 / 17 | 0.98 | 0.00 | 0-6 |
| 260 Av. Juárez-Balderas | 19 / 19 | 0.00 | 0.97 | 12-19 |
| 026 Reforma - Versalles | 0 / 12 | 0.97 | 0.01 | 0-7 |
| 020 Reforma- Río Támesis | 0 / 20 | 0.96 | 0.00 | 0-8 |
| 010 Reforma - Ramírez | 1 / 26 | 0.91 | 0.00 | 0-6 |
| 116 Londres-Roma | 1 / 23 | 0.83 | 0.00 | 0-7 |
| 085 Rosas Moreno - Sullivan | 1 / 15 | 0.78 | 0.00 | 0-5 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.77 | 0.00 | 0-4 |
| 115 Roma-Dinamarca | 1 / 26 | 0.77 | 0.00 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 3 / 28 | 0.69 | 0.00 | 1-15 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 260 (19/19) a 010 (1/26)
2. Llevar **10 bicis** de 270 (24/28) a 020 (0/20)
3. Llevar **9 bicis** de 259 (24/26) a 008 (0/17)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

392 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
