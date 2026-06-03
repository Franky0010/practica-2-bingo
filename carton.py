"""
Carton: clase base del cartón de Bingo.
Relación con CartónDoble: herencia (CartónDoble ES UN Carton).
"""

import random


class Carton:
    """Cartón de Bingo con 5 columnas de 5 números según la palabra y el rango configurado."""

    def __init__(self, palabra: str = "BINGO", max_num: int = 90) -> None:
        if len(palabra) != 5 or len(set(palabra)) != 5:
            raise ValueError("La palabra debe tener exactamente 5 letras sin repetir.")
        if not (50 <= max_num <= 90) or max_num % 5 != 0:
            raise ValueError("El máximo debe ser múltiplo de 5 entre 50 y 90.")

        self._palabra: str = palabra.upper()
        self._max_num: int = max_num
        self._grilla: dict[str, list[int]] = {}
        self._marcados: set[int] = set()
        self._generar_grilla()

    def _dominios(self) -> list[list[int]]:
        paso = self._max_num // 5
        return [
            list(range(i * paso + 1, (i + 1) * paso + 1))
            for i in range(5)
        ]

    def _generar_grilla(self) -> None:
        for i, letra in enumerate(self._palabra):
            self._grilla[letra] = sorted(random.sample(self._dominios()[i], 5))

    def marcar(self, numero: int) -> bool:
        """Marca el número si existe en el cartón. Retorna True si fue marcado."""
        for nums in self._grilla.values():
            if numero in nums:
                self._marcados.add(numero)
                return True
        return False

    def tiene_bingo(self) -> bool:
        """Bingo cuando alguna columna queda completamente marcada."""
        return any(
            all(n in self._marcados for n in nums)
            for nums in self._grilla.values()
        )

    def progreso(self) -> float:
        """Fracción de números marcados sobre el total (0.0–1.0)."""
        marcados = sum(1 for nums in self._grilla.values() for n in nums if n in self._marcados)
        return marcados / 25

    def total_marcados(self) -> int:
        return sum(1 for nums in self._grilla.values() for n in nums if n in self._marcados)

    def mostrar(self) -> str:
        encabezado = "  ".join(f"{l:^4}" for l in self._palabra)
        lineas = [encabezado, "-" * len(encabezado)]
        for fila in range(5):
            row = []
            for letra in self._palabra:
                n = self._grilla[letra][fila]
                marca = "*" if n in self._marcados else " "
                row.append(f"{n:>2}{marca} ")
            lineas.append(" ".join(row))
        return "\n".join(lineas)

    @property
    def palabra(self) -> str:
        return self._palabra

    @property
    def max_num(self) -> int:
        return self._max_num
