# Sistema de Juego de Bingo

## Descripción

Este proyecto implementa un sistema completo de Bingo utilizando Programación Orientada a Objetos en Python.

El sistema modela los elementos principales del juego como clases independientes que interactúan entre sí, permitiendo simular una partida completa de bingo desde consola.

Se incluyen:

* Cartones de juego
* Jugadores
* Bombo (extracción de números)
* Juego (control de la partida)

Además, se implementa un tipo especial de cartón llamado **CartonDoble**, que contiene dos grillas independientes y permite ganar con cualquiera de ellas.

---

## Cómo ejecutar el proyecto

1. Tener instalado Python 3.11 o superior.
2. Descargar o clonar el repositorio.
3. Abrir la terminal en la carpeta del proyecto.
4. Ejecutar el siguiente comando:

```bash
python main.py
```

---

## Estructura del proyecto

```
Bingo/
├── carton.py
├── carton_doble.py
├── bombo.py
├── jugador.py
├── juego.py
├── main.py
└── README.md
```

---

## Clases implementadas

###  Carton

* Representa un cartón de bingo estándar.
* Genera una grilla de números basada en una palabra de 5 letras.
* Permite marcar números y verificar si se ha completado el bingo.

###  CartonDoble

* Hereda de `Carton`.
* Contiene dos grillas independientes.
* Permite ganar si cualquiera de las dos grillas completa el bingo.
* Permite identificar cuál grilla está más cerca de completarse.

###  Bombo

* Encargado de extraer números aleatorios sin repetición.
* Mantiene un historial de los números extraídos.
* Simula el comportamiento real del bombo en un juego de bingo.

###  Jugador

* Representa un participante del juego.
* Puede tener uno o más cartones.
* Marca números a medida que se extraen.
* Verifica si ha ganado el juego.

###  Juego

* Coordina toda la partida de bingo.
* Controla los turnos del juego.
* Notifica a los jugadores cada número extraído.
* Determina el ganador de la partida.
* Genera un reporte final del juego.

---

##  Relaciones entre clases

### Carton → CartonDoble (Herencia)

CartonDoble es una extensión de la clase Carton, lo que permite reutilizar la lógica existente y añadir nuevas funcionalidades sin duplicar código.

### Juego → Bombo (Composición)

El Bombo es creado dentro de la clase Juego y su ciclo de vida depende completamente del mismo. Si el juego termina, el bombo deja de existir.

### Jugador → Carton (Agregación)

Los cartones pueden existir independientemente del jugador. Un jugador puede agregar o retirar cartones sin que estos desaparezcan.

### Juego → Jugador (Asociación)

El juego mantiene una referencia a los jugadores registrados, pero no los crea ni los destruye. Los jugadores pueden unirse o retirarse del juego.

---

##  Tecnologías utilizadas

* Python 3.11
* Biblioteca estándar de Python (sin uso de librerías externas)

---

##  Consideraciones técnicas

* No se utilizan variables globales.
* Se siguen las convenciones de estilo PEP 8.
* Se utilizan type hints en todas las clases.
* Se implementa manejo básico de excepciones.
* El programa se ejecuta correctamente desde la línea de comandos.

---

##  Ejecución del sistema

El archivo `main.py` actúa como script de demostración:

* Crea un juego
* Registra al menos tres jugadores
* Asigna cartones (incluyendo un CartonDoble)
* Ejecuta la partida turno a turno
* Muestra en consola:

  * Número extraído en cada turno
  * Jugadores que marcan el número
  * Ganador final

---

##  Autor(es)

* FRANKY JULIAN MARRIN VINASCO
* JUAN MANUEL CASTAÑO GUTIÉRREZ

