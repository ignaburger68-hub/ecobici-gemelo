# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 21/11/2026 12:37 (hora de Ciudad de México).

## Último pronóstico: 21/11 12:37 a 13:37

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**21.9 °C** · sin lluvia · viento 2 km/h · día fin de semana

El clima multiplica los **retiros por 0.92** y las **devoluciones por 0.94** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | normal (±1 °C) | 0.977 | 0.981 |
| viento | < 5 km/h | 0.943 | 0.954 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 450 Ramos Arizpe- Av México Teno | 30 / 30 | 0.00 | 0.99 | 27-30 |
| 026 Reforma - Versalles | 0 / 14 | 0.97 | 0.00 | 0-6 |
| 115 Roma-Dinamarca | 0 / 27 | 0.97 | 0.00 | 0-5 |
| 555 Ribera de San Cosme - Insurg | 34 / 35 | 0.00 | 0.83 | 30-35 |
| 260 Av. Juárez-Balderas | 18 / 20 | 0.00 | 0.75 | 14-20 |
| 041 Reforma - Av. de la Repúblic | 1 / 30 | 0.75 | 0.00 | 2-15 |
| 118 Liverpool-Dinamarca | 1 / 17 | 0.70 | 0.00 | 0-4 |
| 010 Reforma - Ramírez | 2 / 25 | 0.63 | 0.00 | 0-7 |
| 255 José Rosas Moreno-Guillermo  | 1 / 33 | 0.63 | 0.00 | 0-4 |
| 259 Tómas Alva Edison-Ponciano A | 25 / 27 | 0.00 | 0.49 | 23-27 |

### Plan recomendado del camión

1. Llevar **10 bicis** de 260 (18/20) a 041 (1/30)
2. Llevar **7 bicis** de 450 (30/30) a 026 (0/14)
3. Llevar **12 bicis** de 555 (34/35) a 115 (0/27)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

322 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

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
