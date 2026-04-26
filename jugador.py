from carton import Carton


class Jugador:
    """
    Representa un jugador de bingo.

    Responsabilidad:
    - Gestionar sus cartones.
    - Marcar números y verificar si gana.

    Relación:
    - Agregación con Carton.
    """

    def __init__(self, nombre: str) -> None:
        self.nombre: str = nombre
        self.cartones: list[Carton] = []
        self.total_marcados: int = 0

    def agregar_carton(self, carton: Carton) -> None:
        """Agrega un cartón al jugador."""
        self.cartones.append(carton)

    def recibir_numero(self, numero: int) -> bool:
        """Marca el número en sus cartones."""
        marco = False

        for carton in self.cartones:
            if carton.marcar_numero(numero):
                self.total_marcados += 1
                marco = True

        return marco

    def tiene_bingo(self) -> bool:
        """Verifica si algún cartón tiene bingo."""
        return any(c.tiene_bingo() for c in self.cartones)