from carton import Carton


class CartonDoble(Carton):
    """
    Representa un cartón doble (dos grillas independientes).

    Responsabilidad:
    - Mantener dos cartones en uno solo.
    - Permitir ganar si cualquiera de las dos grillas completa bingo.

    Relación:
    - Hereda de Carton.
    """

    def __init__(self, palabra: str = "BINGO", maximo: int = 90) -> None:
        super().__init__(palabra, maximo)

        self.grilla_1 = self.grilla
        self.marcados_1 = self.marcados

        self.grilla = {}
        self.marcados = set()
        self._generar_grilla()

        self.grilla_2 = self.grilla
        self.marcados_2 = self.marcados

    def marcar_numero(self, numero: int) -> bool:
        """Marca el número en ambas grillas."""
        marcado = False

        for numeros in self.grilla_1.values():
            if numero in numeros:
                self.marcados_1.add(numero)
                marcado = True

        for numeros in self.grilla_2.values():
            if numero in numeros:
                self.marcados_2.add(numero)
                marcado = True

        return marcado

    def tiene_bingo(self) -> bool:
        """Verifica si alguna de las dos grillas tiene bingo."""
        return self._check(self.grilla_1, self.marcados_1) or self._check(
            self.grilla_2, self.marcados_2
        )

    def _check(self, grilla, marcados) -> bool:
        numeros = {n for col in grilla.values() for n in col}
        return numeros.issubset(marcados)

    def grilla_mas_cercana(self) -> str:
        """Indica cuál grilla está más cerca de completar bingo."""
        f1 = 25 - len(self.marcados_1)
        f2 = 25 - len(self.marcados_2)

        if f1 < f2:
            return "Grilla 1"
        elif f2 < f1:
            return "Grilla 2"
        return "Empate"