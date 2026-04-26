from carton import Carton
from carton_doble import CartonDoble
from jugador import Jugador
from juego import Juego


def main() -> None:
    """Script de demostración del juego de bingo."""

    juego = Juego("BINGO", 90)

    j1 = Jugador("Ana")
    j2 = Jugador("Luis")
    j3 = Jugador("Maria")

    j1.agregar_carton(Carton())
    j2.agregar_carton(CartonDoble())
    j3.agregar_carton(Carton())

    juego.registrar_jugador(j1)
    juego.registrar_jugador(j2)
    juego.registrar_jugador(j3)

    juego.jugar()


if __name__ == "__main__":
    main()