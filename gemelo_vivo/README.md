# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 20:29 (hora de Ciudad de México).

## Último pronóstico: 23/11 20:28 a 21:28

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**15.1 °C** · lluvia 0.1 mm/h · viento 2 km/h · día hábil

El clima multiplica los **retiros por 0.88** y las **devoluciones por 0.91** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | ligera (<1 mm/h) | 0.945 | 0.967 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 260 Av. Juárez-Balderas | 21 / 21 | 0.00 | 1.00 | 18-21 |
| 450 Ramos Arizpe- Av México Teno | 31 / 31 | 0.00 | 1.00 | 29-31 |
| 048 Independencia - Azueta | 11 / 11 | 0.00 | 0.99 | 9-11 |
| 117 Londres-Nápoles | 0 / 30 | 0.98 | 0.00 | 0-5 |
| 026 Reforma - Versalles | 13 / 14 | 0.00 | 0.88 | 11-14 |
| 555 Ribera de San Cosme - Insurg | 30 / 33 | 0.00 | 0.86 | 29-33 |
| 086 Sullivan-Insurgentes | 13 / 16 | 0.00 | 0.80 | 12-16 |
| 256 Gómez Farías-Sadi Carnot | 21 / 23 | 0.00 | 0.68 | 19-23 |
| 029 Reforma - Bucareli | 30 / 34 | 0.00 | 0.68 | 30-34 |

### Plan recomendado del camión

1. Llevar **16 bicis** de 260 (21/21) a 117 (0/30)
2. Llevar **19 bicis** de 555 (30/33) a 031 (2/36)
3. Llevar **10 bicis** de 450 (31/31) a 008 (2/16)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

497 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.117 | 0.031 |
| Sin resincronizar | 0.252 | 0.088 |
| Persistencia | 0.288 | 0.060 |
| Persistencia 0/1 | 0.288 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
