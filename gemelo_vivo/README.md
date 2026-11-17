# Gemelo digital Ecobici · en vivo

Página actualizada automáticamente el 16/11/2026 20:46 (hora de Ciudad de México).

## Último pronóstico: 16/11 20:46 a 21:46

![Mapa](ultimo/mapa.png)

### Clima de la hora y su efecto en la demanda

**14.3 °C** · sin lluvia · viento 8 km/h · día fin de semana

El clima multiplica los **retiros por 0.78** y las **devoluciones por 0.84** (1,00 = sin efecto).

| Variable | Condición | Factor retiros | Factor devoluciones |
| --- | --- | --- | --- |
| lluvia | sin lluvia | 0.991 | 0.996 |
| lluvia previa | seco antes | 1.006 | 1.009 |
| temperatura | más frío (−3 a −1 °C) | 0.843 | 0.875 |
| viento | 5-10 km/h | 0.930 | 0.955 |

| Estación | Bicis / capacidad | P(vacía) | P(llena) | Bicis en 1 h (IC 80 %) |
| --- | --- | --- | --- | --- |
| 255 José Rosas Moreno-Guillermo  | 0 / 28 | 0.99 | 0.00 | 0-2 |
| 003 Reforma - Insurgentes | 0 / 31 | 0.95 | 0.00 | 0-6 |
| 041 Reforma - Av. de la Repúblic | 0 / 23 | 0.95 | 0.00 | 0-7 |
| 020 Reforma- Río Támesis | 11 / 12 | 0.00 | 0.77 | 7-12 |
| 116 Londres-Roma | 17 / 18 | 0.00 | 0.73 | 16-18 |
| 555 Ribera de San Cosme - Insurg | 1 / 31 | 0.68 | 0.00 | 0-4 |
| 048 Independencia - Azueta | 8 / 9 | 0.00 | 0.66 | 5-9 |
| 113 General Prim-Versalles | 9 / 10 | 0.00 | 0.55 | 7-10 |
| 118 Liverpool-Dinamarca | 15 / 16 | 0.00 | 0.41 | 13-16 |
| 026 Reforma - Versalles | 8 / 11 | 0.01 | 0.30 | 5-11 |

### Plan recomendado del camión

1. Llevar **7 bicis** de 020 (11/12) a 041 (0/23)
2. Llevar **10 bicis** de 116 (17/18) a 003 (0/31)
3. Llevar **4 bicis** de 048 (8/9) a 255 (0/28)

## ¿Qué tan bien pronostica? (pronósticos hechos en tiempo real, ya evaluados)

1 pronósticos evaluados contra lo que ocurrió una hora después (sin estaciones con camión del operador). Menor es mejor; decir siempre 50 % da 0,25.

| Modelo | Brier vacía | Brier llena |
| --- | --- | --- |
| Gemelo | nan | nan |
| Sin resincronizar | nan | nan |
| Persistencia | nan | nan |
| Persistencia 0/1 | nan | nan |

![Brier por día](brier_vivo.png)

## Detalle

![Abanico](ultimo/abanico.png)

Archivos: `pronosticos.csv` (cada pronóstico), `evaluaciones.csv` (lo que ocurrió), `resumen_vivo.csv` (puntajes), `ultimo/` (tablas y resumen del último ciclo).
