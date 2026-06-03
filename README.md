# Práctica 2 – Sistema de Juego de Bingo
**Juan Manuel Castaño Gutiérrez — Franky Julian Marrin Vinasco**

## Ejecución

```bash
cd practica2
python main.py
```

Requiere Python 3.11 o superior. No se usan librerías externas.

## Estructura del proyecto

```
practica2/
├── carton.py        # Clase base Carton
├── carton_doble.py  # CartónDoble (hereda de Carton)
├── bombo.py         # Bombo (composición con Juego)
├── jugador.py       # Jugador (asociación con Carton)
├── juego.py         # Juego (director de la partida)
└── main.py          # Demostración ejecutable
```

## Clases implementadas

### Carton (`carton.py`)
- **Atributos:** `_palabra`, `_max_num`, `_grilla`, `_marcados`
- **Métodos:** `marcar()`, `tiene_bingo()`, `progreso()`, `total_marcados()`, `mostrar()`

### CartónDoble (`carton_doble.py`)
- **Atributos heredados** + `_grilla2`, `_marcados2`
- **Métodos sobrescritos:** `marcar()`, `tiene_bingo()`
- **Métodos propios:** `grilla_mas_cercana()`, `_mostrar_grilla2()`

### Bombo (`bombo.py`)
- **Atributos:** `_max_num`, `_disponibles`, `_historial`
- **Métodos:** `extraer()`, `tiene_numeros()`

### Jugador (`jugador.py`)
- **Atributos:** `_nombre`, `_cartones`, `_total_marcados`
- **Métodos:** `agregar_carton()`, `retirar_carton()`, `marcar_numero()`, `tiene_bingo()`

### Juego (`juego.py`)
- **Atributos:** `_palabra`, `_max_num`, `_bombo`, `_jugadores`, `_ganadores`
- **Métodos:** `registrar_jugador()`, `dar_baja_jugador()`, `ejecutar_turno()`, `hay_ganador()`, `reporte_final()`

## Justificación de relaciones entre clases

**Carton ↔ CartónDoble — Herencia**
CartónDoble es un tipo especial de Carton: reutiliza toda su lógica de generación de grilla y marcado, y solo añade una segunda grilla independiente. La relación "es-un" justifica la herencia: CartónDoble no duplica código, sino que extiende el comportamiento con `tiene_bingo()` y `grilla_mas_cercana()`.

**Juego ↔ Bombo — Composición**
El Bombo no tiene sentido fuera de una partida: se instancia dentro del constructor de Juego y su ciclo de vida está totalmente ligado al del Juego. Si la partida termina (el objeto Juego deja de existir), el Bombo también desaparece. El mecanismo que establece esta relación es la instanciación directa en `__init__`: `self._bombo = Bombo(max_num)`.

**Jugador ↔ Cartón(es) — Asociación**
Los cartones se generan externamente y se asignan a los jugadores mediante `agregar_carton()`. Un cartón puede existir sin estar asignado a ningún jugador, y si un jugador abandona la partida, sus cartones no desaparecen. El mecanismo es una lista de referencias: `self._cartones: list[Carton]`.

**Juego ↔ Jugador(es) — Asociación**
El Juego no crea ni destruye jugadores: simplemente los referencia. Los jugadores se registran voluntariamente con `registrar_jugador()` y pueden darse de baja en cualquier momento. El mecanismo es una lista de referencias: `self._jugadores: list[Jugador]`.

##  Autor(es)

* FRANKY JULIAN MARRIN VINASCO
* JUAN MANUEL CASTAÑO GUTIÉRREZ

