# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 13:48 (hora de Ciudad de México).

## Último pronóstico: 21/11 13:48 a 14:48

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**23.4 °C** · sin lluvia · viento 3 km/h · día fin de semana

El clima multiplica los **retiros por 0.96** y las **devoluciones por 0.99** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más cálido (1 a 3 °C) | 1.039 | 1.054 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 15 | 0.99 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 35 / 35 | 0.00 | 0.98 | 26-34 |
| 260 Av. Juárez-Balderas | 19 / 20 | 0.00 | 0.83 | 14-20 |
| 041 Reforma - Av. de la Repúblic | 1 / 31 | 0.80 | 0.00 | 0-8 |
| 115 Roma-Dinamarca | 1 / 27 | 0.78 | 0.00 | 0-6 |
| 012 Río Lerma - Villalongín | 1 / 15 | 0.76 | 0.00 | 0-5 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.73 | 0.00 | 0-4 |
| 020 Reforma- Río Támesis | 2 / 23 | 0.58 | 0.00 | 0-6 |
| 010 Reforma - Ramírez | 3 / 27 | 0.57 | 0.00 | 0-8 |
| 450 Ramos Arizpe- Av México Teno | 27 / 30 | 0.00 | 0.48 | 23-30 |

### Plan recomendado del camión

1. Llevar **15 bicis** de 555 (35/35) a 041 (1/31)
2. Llevar **8 bicis** de 260 (19/20) a 085 (0/15)
3. Llevar **12 bicis** de 270 (27/31) a 115 (1/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

327 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
