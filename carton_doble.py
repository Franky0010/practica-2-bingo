"""
CartónDoble: extiende Carton con dos grillas independientes.
Relación con Carton: herencia (CartónDoble ES UN Carton, no duplica lógica).
"""

import random
from carton import Carton


class CartonDoble(Carton):
    """Cartón con dos grillas generadas con los mismos parámetros. Gana si completa cualquiera."""

    def __init__(self, palabra: str = "BINGO", max_num: int = 90) -> None:
        super().__init__(palabra, max_num)
        self._grilla2: dict[str, list[int]] = {}
        self._marcados2: set[int] = set()
        self._generar_grilla2()

    def _generar_grilla2(self) -> None:
        paso = self._max_num // 5
        for i, letra in enumerate(self._palabra):
            dominio = list(range(i * paso + 1, (i + 1) * paso + 1))
            self._grilla2[letra] = sorted(random.sample(dominio, 5))

    def marcar(self, numero: int) -> bool:
        """Marca el número en ambas grillas si aparece. Retorna True si fue marcado en alguna."""
        marcado1 = super().marcar(numero)
        marcado2 = False
        for nums in self._grilla2.values():
            if numero in nums:
                self._marcados2.add(numero)
                marcado2 = True
                break
        return marcado1 or marcado2

    def tiene_bingo(self) -> bool:
        """Retorna True si alguna de las dos grillas tiene una columna completa."""
        bingo_grilla1 = super().tiene_bingo()
        bingo_grilla2 = any(
            all(n in self._marcados2 for n in nums)
            for nums in self._grilla2.values()
        )
        return bingo_grilla1 or bingo_grilla2

    def grilla_mas_cercana(self) -> int:
        """Indica qué grilla (1 o 2) está más cerca de completarse."""
        prog1 = self.progreso()
        marcados2 = sum(1 for nums in self._grilla2.values() for n in nums if n in self._marcados2)
        prog2 = marcados2 / 25
        return 1 if prog1 >= prog2 else 2

    def mostrar(self) -> str:
        g2_lineas = self._mostrar_grilla2()
        return f"[Grilla 1]\n{super().mostrar()}\n[Grilla 2]\n{g2_lineas}"

    def _mostrar_grilla2(self) -> str:
        encabezado = "  ".join(f"{l:^4}" for l in self._palabra)
        lineas = [encabezado, "-" * len(encabezado)]
        for fila in range(5):
            row = []
            for letra in self._palabra:
                n = self._grilla2[letra][fila]
                marca = "*" if n in self._marcados2 else " "
                row.append(f"{n:>2}{marca} ")
            lineas.append(" ".join(row))
        return "\n".join(lineas)
