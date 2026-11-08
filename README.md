# ecobici-gemelo

## Funcionamiento
Este código está diseñado para poder obtener la información a tiempo real de cada estación de bici de Ecobici, esta información se encuentra disponible para uso público según lo que indica la pagina web. Como tal publica los datos del sistema en tiempo real sobre la disponibilidad de bicicletas y cicloestaciones con el estándar GBFS (General Bikeshare Feed Specification)


## Obtención de datos
Cada 30min el sistema recupera el estado de cada estación (registrada cada minuto que pasaron), el sistema está configurada para que termine en 6 horas, pero tras esto se retoma y sigue obteniendo datos de manera indefinida


## Pagina web
Pueden visitar la pagina https://ecobici.cdmx.gob.mx/datos-abiertos/ que es en donde se enucuentra mayor informacion de la base de dato y los permisos correspondientes.
