# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 17/11/2026 20:58 (hora de Ciudad de México).

## Último pronóstico: 17/11 20:58 a 21:58

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.1 °C** · sin lluvia · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.71** y las **devoluciones por 0.77** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 086 Sullivan-Insurgentes | 0 / 3 | 1.00 | 0.60 | 0-3 |
| 020 Reforma- Río Támesis | 0 / 8 | 0.99 | 0.00 | 0-2 |
| 450 Ramos Arizpe- Av México Teno | 27 / 27 | 0.00 | 0.99 | 24-27 |
| 008 Reforma - General Prim | 0 / 17 | 0.99 | 0.00 | 0-4 |
| 041 Reforma - Av. de la Repúblic | 1 / 20 | 0.97 | 0.00 | 0-5 |
| 010 Reforma - Ramírez | 2 / 27 | 0.96 | 0.00 | 0-2 |
| 117 Londres-Nápoles | 1 / 30 | 0.90 | 0.00 | 0-3 |
| 116 Londres-Roma | 1 / 16 | 0.89 | 0.00 | 0-4 |
| 113 General Prim-Versalles | 0 / 10 | 0.85 | 0.03 | 0-6 |
| 085 Rosas Moreno - Sullivan | 1 / 14 | 0.84 | 0.00 | 0-5 |

### Plan recomendado del camión

1. Llevar **20 bicis** de 450 (27/27) a 010 (2/27)
2. Llevar **13 bicis** de 555 (26/29) a 041 (1/20)
3. Llevar **7 bicis** de 259 (18/24) a 020 (0/8)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

73 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.130 | 0.028 |
| Sin resincronizar | 0.322 | 0.092 |
| Persistencia | 0.371 | 0.049 |
| Persistencia 0/1 | 0.371 | 0.049 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
