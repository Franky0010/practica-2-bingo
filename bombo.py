"""
Bombo: mecanismo de extracción de números.
Relación con Juego: composición (el Bombo no existe fuera del Juego).
"""

import random


class Bombo:
    """Extrae números aleatorios sin repetición y registra el historial de la partida."""

    def __init__(self, max_num: int = 90) -> None:
        if not (50 <= max_num <= 90) or max_num % 5 != 0:
            raise ValueError("El máximo debe ser múltiplo de 5 entre 50 y 90.")
        self._max_num: int = max_num
        self._disponibles: list[int] = list(range(1, max_num + 1))
        self._historial: list[int] = []

    def extraer(self) -> int:
        """Extrae y retorna un número aleatorio de los disponibles."""
        if not self._disponibles:
            raise RuntimeError("El bombo está vacío; no quedan números por extraer.")
        numero = random.choice(self._disponibles)
        self._disponibles.remove(numero)
        self._historial.append(numero)
        return numero

    def tiene_numeros(self) -> bool:
        return len(self._disponibles) > 0

    @property
    def historial(self) -> list[int]:
        return list(self._historial)

    @property
    def max_num(self) -> int:
        return self._max_num
