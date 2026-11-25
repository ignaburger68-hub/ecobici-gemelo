# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 20:38 (hora de Ciudad de México).

## Último pronóstico: 24/11 20:38 a 21:38

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.3 °C** · lluvia 0.8 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.52** y las **devoluciones por 0.59** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 450 Ramos Arizpe- Av México Teno | 30 / 31 | 0.00 | 0.84 | 29-31 |
| 098 Emilio Dondé-Av. Balderas | 30 / 31 | 0.00 | 0.78 | 28-31 |
| 555 Ribera de San Cosme - Insurg | 32 / 34 | 0.00 | 0.67 | 27-34 |
| 113 General Prim-Versalles | 1 / 15 | 0.63 | 0.00 | 0-5 |
| 116 Londres-Roma | 1 / 23 | 0.62 | 0.00 | 0-5 |
| 260 Av. Juárez-Balderas | 17 / 21 | 0.00 | 0.45 | 15-21 |
| 086 Sullivan-Insurgentes | 11 / 16 | 0.00 | 0.32 | 9-16 |
| 003 Reforma - Insurgentes | 3 / 30 | 0.29 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 11 / 15 | 0.00 | 0.20 | 8-14 |
| 029 Reforma - Bucareli | 28 / 35 | 0.00 | 0.11 | 26-34 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 450 (30/31) a 116 (1/23)
2. Llevar **8 bicis** de 555 (32/34) a 113 (1/15)
3. Llevar **11 bicis** de 098 (30/31) a 003 (3/30)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

569 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.115 | 0.033 |
| Sin resincronizar | 0.243 | 0.084 |
| Persistencia | 0.271 | 0.061 |
| Persistencia 0/1 | 0.271 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
