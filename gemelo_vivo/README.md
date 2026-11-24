# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 23/11/2026 21:11 (hora de Ciudad de México).

## Último pronóstico: 23/11 21:11 a 22:11

![Mapa](ultimo/mapa.png)

### Clima pronosticado de la hora y su efecto en la demanda

_La hora todavía no termina: el clima es el pronóstico meteorológico (Open-Meteo)._

**14.6 °C** · sin lluvia · viento 4 km/h · día hábil

El clima multiplica los **retiros por 0.91** y las **devoluciones por 0.92** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.988 | 0.981 |
| lluvia previa | seco antes | 0.990 | 1.001 |
| temperatura | normal (±1 °C) | 0.944 | 0.951 |
| viento | < 5 km/h | 0.988 | 0.985 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 085 Rosas Moreno - Sullivan | 0 / 5 | 1.00 | 0.00 | 0-0 |
| 048 Independencia - Azueta | 11 / 11 | 0.00 | 0.99 | 9-11 |
| 026 Reforma - Versalles | 13 / 13 | 0.00 | 0.97 | 9-13 |
| 086 Sullivan-Insurgentes | 15 / 16 | 0.00 | 0.91 | 12-16 |
| 260 Av. Juárez-Balderas | 20 / 21 | 0.00 | 0.84 | 18-21 |
| 450 Ramos Arizpe- Av México Teno | 29 / 31 | 0.00 | 0.81 | 29-31 |
| 555 Ribera de San Cosme - Insurg | 29 / 33 | 0.00 | 0.69 | 28-33 |
| 117 Londres-Nápoles | 1 / 30 | 0.69 | 0.00 | 0-4 |
| 256 Gómez Farías-Sadi Carnot | 20 / 22 | 0.00 | 0.63 | 18-22 |
| 255 José Rosas Moreno-Guillermo  | 29 / 34 | 0.00 | 0.37 | 29-34 |

### Plan recomendado del camión

1. Llevar **11 bicis** de 086 (15/16) a 117 (1/30)
2. Llevar **19 bicis** de 555 (29/33) a 031 (2/36)
3. Llevar **8 bicis** de 048 (11/11) a 010 (7/26)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

500 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | 0.117 | 0.031 |
| Sin resincronizar | 0.250 | 0.088 |
| Persistencia | 0.286 | 0.060 |
| Persistencia 0/1 | 0.286 | 0.060 |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
