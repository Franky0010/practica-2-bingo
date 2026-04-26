from bombo import Bombo
from jugador import Jugador


class Juego:
    """
    Representa la partida de bingo.

    Responsabilidad:
    - Coordinar el juego.
    - Ejecutar turnos.
    - Determinar ganador.

    Relación:
    - Composición con Bombo.
    - Asociación con Jugador.
    """

    def __init__(self, palabra: str = "BINGO", maximo: int = 90) -> None:
        self.bombo: Bombo = Bombo(maximo)
        self.jugadores: list[Jugador] = []
        self.ganador: Jugador | None = None
        self.turnos: int = 0

    def registrar_jugador(self, jugador: Jugador) -> None:
        self.jugadores.append(jugador)

    def ejecutar_turno(self) -> None:
        numero = self.bombo.extraer_numero()
        self.turnos += 1

        print(f"\nTurno {self.turnos}")
        print(f"Numero extraido: {numero}")

        for jugador in self.jugadores:
            if jugador.recibir_numero(numero):
                print(f"{jugador.nombre} marco el numero {numero}")

            if jugador.tiene_bingo():
                self.ganador = jugador
                print(f"\nGANADOR: {jugador.nombre}")
                return

    def jugar(self) -> None:
        while self.bombo.quedan_numeros() and self.ganador is None:
            self.ejecutar_turno()