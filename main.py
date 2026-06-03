"""
Script de demostración: partida de Bingo con 3 jugadores y un CartónDoble.
Ejecutar: python main.py
"""

from carton import Carton
from carton_doble import CartonDoble
from jugador import Jugador
from juego import Juego


def main() -> None:
    palabra = "BINGO"
    max_num = 90

    # --- Cartones (existen antes e independientemente de los jugadores) ---
    c1 = Carton(palabra, max_num)
    c2 = Carton(palabra, max_num)
    c3 = CartonDoble(palabra, max_num)   # cartón doble
    c4 = Carton(palabra, max_num)

    # --- Jugadores (asociación con cartones) ---
    juan = Jugador("Juan")
    juan.agregar_carton(c1)

    maria = Jugador("María")
    maria.agregar_carton(c2)
    maria.agregar_carton(c3)   # posee también el cartón doble

    pedro = Jugador("Pedro")
    pedro.agregar_carton(c4)

    # --- Juego (composición con Bombo; asociación con jugadores) ---
    juego = Juego(palabra, max_num)
    juego.registrar_jugador(juan)
    juego.registrar_jugador(maria)
    juego.registrar_jugador(pedro)

    print("=" * 45)
    print(f"  BINGO  |  Palabra: {palabra}  |  Máx: {max_num}")
    print("=" * 45)
    print(f"Jugadores: Juan (1 cartón), María (2 cartones, 1 doble), Pedro (1 cartón)\n")

    print("--- Cartones iniciales ---")
    print(f"\nJuan - Cartón 1:\n{c1.mostrar()}")
    print(f"\nMaría - Cartón 2:\n{c2.mostrar()}")
    print(f"\nMaría - Cartón Doble:\n{c3.mostrar()}")
    print(f"\nPedro - Cartón 4:\n{c4.mostrar()}")
    print("\n" + "=" * 45)
    print("           INICIO DE LA PARTIDA")
    print("=" * 45 + "\n")

    turno = 0
    while not juego.hay_ganador():
        turno += 1
        resultado = juego.ejecutar_turno()

        if resultado.get("estado") == "sin_numeros":
            print("Se agotaron todos los números sin ganador.")
            break

        numero = resultado["numero"]
        marcadores = resultado["marcadores"]
        ganadores = resultado["ganadores"]

        marcadores_str = f"  <- {', '.join(marcadores)}" if marcadores else ""
        print(f"Turno {turno:>3}: [{numero:>2}]{marcadores_str}")

        if ganadores:
            print(f"\n{'!'*10} BINGO {'!'*10}")
            print(f"Ganador(es): {', '.join(ganadores)}")
            break

    # Mostrar cartones finales del ganador
    for jugador in [juan, maria, pedro]:
        if jugador.tiene_bingo():
            print(f"\n--- Cartones finales de {jugador.nombre} ---")
            for i, carton in enumerate(jugador.cartones, 1):
                print(f"\nCartón {i}:\n{carton.mostrar()}")

    print(juego.reporte_final())


if __name__ == "__main__":
    main()
