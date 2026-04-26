import random


class Carton:
    """
    Representa un cartón de bingo estándar.

    Responsabilidad:
    - Generar una grilla de números según una palabra de 5 letras.
    - Permitir marcar números y verificar si tiene bingo.

    Relación:
    - Es clase base de CartonDoble (herencia).
    - Puede ser asociado a un Jugador (agregación).
    """

    def __init__(self, palabra: str = "BINGO", maximo: int = 90) -> None:
        self.palabra: str = palabra.upper()
        self.maximo: int = maximo
        self.grilla: dict[str, list[int]] = {}
        self.marcados: set[int] = set()

        self._validar_parametros()
        self._generar_grilla()

    def _validar_parametros(self) -> None:
        """Valida que la palabra y el rango sean correctos."""
        if len(self.palabra) != 5:
            raise ValueError("La palabra debe tener 5 letras")

        if len(set(self.palabra)) != 5:
            raise ValueError("No se permiten letras repetidas")

        if self.maximo < 50 or self.maximo > 90 or self.maximo % 5 != 0:
            raise ValueError("El máximo debe ser múltiplo de 5 entre 50 y 90")

    def _generar_grilla(self) -> None:
        """Genera los números del cartón distribuidos por columnas."""
        cantidad = self.maximo // 5
        inicio = 1

        for letra in self.palabra:
            fin = inicio + cantidad
            self.grilla[letra] = sorted(random.sample(range(inicio, fin), 5))
            inicio = fin

    def marcar_numero(self, numero: int) -> bool:
        """Marca un número si existe en el cartón."""
        for numeros in self.grilla.values():
            if numero in numeros:
                self.marcados.add(numero)
                return True
        return False

    def tiene_bingo(self) -> bool:
        """Verifica si todos los números del cartón han sido marcados."""
        numeros = {n for col in self.grilla.values() for n in col}
        return numeros.issubset(self.marcados)

    def mostrar(self) -> None:
        """Imprime el cartón en consola."""
        for letra, numeros in self.grilla.items():
            print(f"{letra}: {numeros}")