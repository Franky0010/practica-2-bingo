import random


class Bombo:
    """
    Representa el bombo de bingo.

    Responsabilidad:
    - Extraer números aleatorios sin repetición.
    - Mantener historial de números extraídos.

    Relación:
    - Es parte del Juego (composición).
    """

    def __init__(self, maximo: int = 90) -> None:
        self.disponibles: list[int] = list(range(1, maximo + 1))
        self.historial: list[int] = []

    def extraer_numero(self) -> int:
        """Extrae un número aleatorio del bombo."""
        if not self.disponibles:
            raise RuntimeError("No quedan números")

        numero = random.choice(self.disponibles)
        self.disponibles.remove(numero)
        self.historial.append(numero)

        return numero

    def quedan_numeros(self) -> bool:
        """Indica si aún quedan números por extraer."""
        return len(self.disponibles) > 0