# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 11:40 (hora de Ciudad de México).

## Último pronóstico: 21/11 11:40 a 12:40

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.5 °C** · sin lluvia · viento 3 km/h · día fin de semana

El clima multiplica los **retiros por 0.92** y las **devoluciones por 0.94** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 450 Ramos Arizpe- Av México Teno | 30 / 30 | 0.00 | 0.99 | 26-30 |
| 085 Rosas Moreno - Sullivan | 0 / 15 | 0.99 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 0 / 25 | 0.98 | 0.00 | 0-6 |
| 270 De la República-Ponciano Arr | 29 / 30 | 0.00 | 0.93 | 24-30 |
| 118 Liverpool-Dinamarca | 1 / 17 | 0.70 | 0.00 | 0-4 |
| 116 Londres-Roma | 2 / 23 | 0.57 | 0.00 | 0-6 |
| 020 Reforma- Río Támesis | 3 / 23 | 0.46 | 0.00 | 1-10 |
| 026 Reforma - Versalles | 3 / 14 | 0.37 | 0.02 | 1-9 |
| 041 Reforma - Av. de la Repúblic | 4 / 31 | 0.36 | 0.01 | 2-18 |
| 260 Av. Juárez-Balderas | 13 / 21 | 0.00 | 0.32 | 11-21 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 270 (29/30) a 010 (0/25)
2. Llevar **8 bicis** de 450 (30/30) a 085 (0/15)
3. Llevar **7 bicis** de 260 (13/21) a 116 (2/23)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

318 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
