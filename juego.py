"""
Juego: director de la partida de Bingo.
Relación con Bombo: composición (el Bombo se crea y destruye con el Juego).
Relación con Jugador: asociación (el Juego los referencia, no los crea ni destruye).
"""

from bombo import Bombo
from jugador import Jugador


class Juego:
    """Coordina la partida: gestiona jugadores, extrae números y determina ganadores."""

    def __init__(self, palabra: str = "BINGO", max_num: int = 90) -> None:
        if len(palabra) != 5 or len(set(palabra)) != 5:
            raise ValueError("La palabra debe tener exactamente 5 letras sin repetir.")
        if not (50 <= max_num <= 90) or max_num % 5 != 0:
            raise ValueError("El máximo debe ser múltiplo de 5 entre 50 y 90.")

        self._palabra: str = palabra.upper()
        self._max_num: int = max_num
        self._bombo: Bombo = Bombo(max_num)        # composición
        self._jugadores: list[Jugador] = []        # asociación
        self._ganadores: list[Jugador] = []

    def registrar_jugador(self, jugador: Jugador) -> None:
        if jugador not in self._jugadores:
            self._jugadores.append(jugador)

    def dar_baja_jugador(self, jugador: Jugador) -> None:
        if jugador in self._jugadores:
            self._jugadores.remove(jugador)

    def ejecutar_turno(self) -> dict:
        """
        Extrae un número, lo notifica a todos los jugadores y detecta ganadores.
        Retorna un dict con: numero, marcadores, ganadores, historial.
        """
        if not self._bombo.tiene_numeros():
            return {"estado": "sin_numeros", "historial": self._bombo.historial}

        numero = self._bombo.extraer()
        marcadores: list[str] = []

        for jugador in self._jugadores:
            if jugador.marcar_numero(numero):
                marcadores.append(jugador.nombre)
            if jugador.tiene_bingo() and jugador not in self._ganadores:
                self._ganadores.append(jugador)

        return {
            "numero": numero,
            "marcadores": marcadores,
            "ganadores": [j.nombre for j in self._ganadores],
            "historial": self._bombo.historial,
        }

    def hay_ganador(self) -> bool:
        return len(self._ganadores) > 0

    def reporte_final(self) -> str:
        lineas = ["\n========== REPORTE FINAL =========="]
        lineas.append(f"Palabra: {self._palabra}  |  Máximo: {self._max_num}")
        lineas.append(f"Números extraídos: {len(self._bombo.historial)}")
        lineas.append(f"Historial: {self._bombo.historial}")
        lineas.append("")
        if self._ganadores:
            lineas.append(f"Ganador(es): {', '.join(j.nombre for j in self._ganadores)}")
        else:
            lineas.append("No hubo ganadores en esta partida.")
        lineas.append("")
        for jugador in self._jugadores:
            n_cartones = len(jugador.cartones)
            lineas.append(
                f"  {jugador.nombre}: {jugador.total_marcados} marcas "
                f"en {n_cartones} cartón(es)"
            )
        lineas.append("====================================")
        return "\n".join(lineas)

    @property
    def palabra(self) -> str:
        return self._palabra

    @property
    def max_num(self) -> int:
        return self._max_num
