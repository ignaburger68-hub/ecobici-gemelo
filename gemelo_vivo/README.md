# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 24/11/2026 20:52 (hora de Ciudad de México).

## Último pronóstico: 24/11 20:52 a 21:52

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**13.3 °C** · lluvia 0.8 mm/h · viento 6 km/h · día hábil

El clima multiplica los **retiros por 0.54** y las **devoluciones por 0.61** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | llovió en las 3 h previas | 0.816 | 0.829 |
| temperatura | más frío (−3 a −1 °C) | 0.841 | 0.872 |
| viento | 5-10 km/h | 0.872 | 0.905 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 098 Emilio Dondé-Av. Balderas | 31 / 31 | 0.00 | 1.00 | 29-31 |
| 116 Londres-Roma | 0 / 23 | 0.97 | 0.00 | 0-6 |
| 450 Ramos Arizpe- Av México Teno | 29 / 30 | 0.00 | 0.93 | 29-30 |
| 003 Reforma - Insurgentes | 2 / 31 | 0.50 | 0.00 | 0-6 |
| 113 General Prim-Versalles | 1 / 15 | 0.48 | 0.00 | 0-6 |
| 026 Reforma - Versalles | 13 / 15 | 0.00 | 0.42 | 9-15 |
| 260 Av. Juárez-Balderas | 16 / 21 | 0.00 | 0.34 | 15-21 |
| 029 Reforma - Bucareli | 29 / 34 | 0.00 | 0.30 | 27-34 |
| 555 Ribera de San Cosme - Insurg | 28 / 34 | 0.00 | 0.23 | 24-34 |
| 086 Sullivan-Insurgentes | 10 / 17 | 0.00 | 0.20 | 7-16 |

### Plan recomendado del camión

1. Llevar **12 bicis** de 450 (29/30) a 116 (0/23)
2. Llevar **12 bicis** de 098 (31/31) a 003 (2/31)
3. Llevar **6 bicis** de 029 (29/34) a 113 (1/15)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

570 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.114 | 0.033 |
| Sin resincronizar | 0.242 | 0.084 |
| Persistencia | 0.271 | 0.061 |
| Persistencia 0/1 | 0.271 | 0.061 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
