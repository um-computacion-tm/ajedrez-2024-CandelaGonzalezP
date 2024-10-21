# Ajedrez orientado a objetos -2024

## Alumno: Candela Gonzalez Privitera
## Legajo: 63007

# Circleci Badge
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-CandelaGonzalezP/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-CandelaGonzalezP/tree/main)

# Maintainability
<a href="https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-CandelaGonzalezP/maintainability"><img src="https://api.codeclimate.com/v1/badges/80e898285edf9282fd84/maintainability" /></a>

# Test Coverage
<a href="https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-CandelaGonzalezP/test_coverage"><img src="https://api.codeclimate.com/v1/badges/80e898285edf9282fd84/test_coverage" /></a>

#################################

### Acerca del proyecto:

Este proyecto es un juego de ajedrez desarrollado en Python utilizando programación orientada a objetos (OOP). El diseño se centra en la modularidad y flexibilidad, permitiendo representar fielmente las reglas del ajedrez y facilitar futuras mejoras. El tablero y las piezas están modelados mediante clases que gestionan el comportamiento y los movimientos de las piezas de manera independiente.

### Contenido y caracteristicas

- Piezas: Cada una de las piezas está implementada como una clase separada (por ejemplo, Pawn, Rook, Knight, Bishop, Queen, King), con métodos que definen sus movimientos permitidos.
- Movimientos: El juego respeta las reglas de movimiento de cada pieza, permitiendo acciones como capturas y movimientos válidos en el tablero.
- Turnos: El juego controla los turnos alternos de los jugadores y permite la interacción a través de la consola.
- Pruebas unitarias: Se han implementado tests para asegurar que los movimientos y las reglas del juego funcionen correctamente. Cada clase de pieza está probada en diferentes escenarios, como movimientos válidos, movimientos bloqueados por otras piezas y capturas.
- Docker: El proyecto incluye soporte para Docker, lo que facilita tanto el testing como el despliegue en diferentes entornos.

### Instrucciones

El jugador con las piezas blancas siempre comienza el juego. Para realizar un movimiento, cada jugador debe especificar la fila y columna de la pieza a mover, así como las coordenadas de destino. Los jugadores se alternan por turnos, siguiendo las reglas estándar de movimiento de cada pieza: peones avanzan pero capturan en diagonal, torres se mueven en líneas rectas, caballos en "L", alfiles en diagonal, la reina en cualquier dirección, y el rey un casillero en cualquier dirección.

### Requisitos

Para correr el juego se requiere [Docker](https://docs.docker.com) 

### Instalación Docker (terminal):

Instalación de Docker

```bash
sudo apt install docker
```

Clonar el [repositorio] (https://github.com/um-computacion-tm/ajedrez-2024-CandelaGonzalezP.git) del juego 

```bash
git clone https://github.com/um-computacion-tm/ajedrez-2024-CandelaGonzalezP.git
```
### Ejecutar el juego

```
python3 -m chess.cli
```

Crear imágen de Docker del juego

```bash
docker buildx build -t ajedrez-2024-CandelaGonzalezP .
```

Ejecutar los tests y el juego

```bash
docker run -i ajedrez-2024-CandelaGonzalezP
```


