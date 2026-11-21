# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 11:26 (hora de Ciudad de México).

## Último pronóstico: 21/11 11:26 a 12:26

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**20.6 °C** · sin lluvia · viento 4 km/h · día fin de semana

El clima multiplica los **retiros por 0.92** y las **devoluciones por 0.94** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 270 De la República-Ponciano Arr | 29 / 29 | 0.00 | 1.00 | 24-29 |
| 116 Londres-Roma | 1 / 22 | 0.76 | 0.00 | 0-5 |
| 118 Liverpool-Dinamarca | 1 / 17 | 0.71 | 0.00 | 0-4 |
| 086 Sullivan-Insurgentes | 1 / 17 | 0.65 | 0.00 | 0-7 |
| 026 Reforma - Versalles | 2 / 14 | 0.53 | 0.01 | 1-8 |
| 085 Rosas Moreno - Sullivan | 2 / 15 | 0.48 | 0.00 | 0-5 |
| 115 Roma-Dinamarca | 2 / 26 | 0.43 | 0.00 | 0-7 |
| 119 Turín-Abraham González | 2 / 29 | 0.39 | 0.00 | 0-7 |
| 260 Av. Juárez-Balderas | 13 / 21 | 0.00 | 0.36 | 12-21 |
| 450 Ramos Arizpe- Av México Teno | 27 / 30 | 0.00 | 0.32 | 24-30 |

### Plan recomendado del camión

1. Llevar **14 bicis** de 270 (29/29) a 116 (1/22)
2. Llevar **8 bicis** de 260 (13/21) a 118 (1/17)
3. Llevar **6 bicis** de 555 (30/35) a 086 (1/17)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

317 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
