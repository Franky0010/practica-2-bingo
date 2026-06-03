"""
Jugador: participante de la partida que posee cartones.
Relación con Carton: asociación (los cartones existen independientemente del jugador).
"""

from carton import Carton


class Jugador:
    """Jugador que puede tener uno o más cartones (incluyendo CartónDoble)."""

    def __init__(self, nombre: str) -> None:
        if not nombre.strip():
            raise ValueError("El nombre del jugador no puede estar vacío.")
        self._nombre: str = nombre
        self._cartones: list[Carton] = []
        self._total_marcados: int = 0

    def agregar_carton(self, carton: Carton) -> None:
        self._cartones.append(carton)

    def retirar_carton(self, carton: Carton) -> None:
        if carton not in self._cartones:
            raise ValueError(f"{self._nombre} no posee ese cartón.")
        self._cartones.remove(carton)

    def marcar_numero(self, numero: int) -> bool:
        """Marca el número en todos sus cartones. Retorna True si fue marcado en alguno."""
        marcado = False
        for carton in self._cartones:
            if carton.marcar(numero):
                self._total_marcados += 1
                marcado = True
        return marcado

    def tiene_bingo(self) -> bool:
        return any(c.tiene_bingo() for c in self._cartones)

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def cartones(self) -> list[Carton]:
        return list(self._cartones)

    @property
    def total_marcados(self) -> int:
        return self._total_marcados

        return any(c.tiene_bingo() for c in self.cartones)
