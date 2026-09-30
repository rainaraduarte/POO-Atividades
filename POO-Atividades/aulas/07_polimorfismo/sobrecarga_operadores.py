"""POO 12 - Sobrecarga de operadores: Ponto com +, -, *, == e str.

Operador          método especial
    a + b         __add__
    a - b         __sub__
    a * k         __mul__
    a == b        __eq__
    print(a)      __str__
    sum([...])    __radd__ (para começar de 0 + Ponto)
"""

from typing import Optional


class Ponto:
    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    def __add__(self, other: "Ponto") -> "Ponto":
        return Ponto(self.__x + other.x, self.__y + other.y)

    def __sub__(self, other: "Ponto") -> "Ponto":
        return Ponto(self.__x - other.x, self.__y - other.y)

    def __mul__(self, k: int) -> "Ponto":
        return Ponto(self.__x * k, self.__y * k)

    def __radd__(self, other: object) -> "Ponto":
        # sum() começa com 0; 0 + Ponto cai aqui
        if other == 0:
            return self
        return NotImplemented

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Ponto):
            return NotImplemented
        return self.__x == other.x and self.__y == other.y

    def __hash__(self) -> int:
        return hash((self.__x, self.__y))

    def __str__(self) -> str:
        return f"Ponto({self.__x}, {self.__y})"


class CalculadoraGeometrica:
    # p3 opcional: "sobrecarga" via parâmetro padrão.
    # Usamos None em vez de Ponto(0, 0) como padrão (evita objeto compartilhado).
    def soma(self, p1: Ponto, p2: Ponto, p3: Optional[Ponto] = None) -> Ponto:
        p3 = p3 if p3 is not None else Ponto(0, 0)
        return Ponto(p1.x + p2.x + p3.x, p1.y + p2.y + p3.y)


if __name__ == "__main__":
    calc = CalculadoraGeometrica()
    p1, p2 = Ponto(1, 2), Ponto(3, 5)

    print("Ponto 1:", p1)
    print("Ponto 2:", p2)
    print("Soma1:", p1 + p2)                       # __add__
    print("Soma2:", calc.soma(p1, p2))
    print("Soma3:", calc.soma(p1, p2, Ponto(1, 1)))
    print("Sub..:", p2 - p1)                       # __sub__
    print("Mul..:", p1 * 3)                        # __mul__
    print(p1 + p2 == Ponto(4, 7))                  # True
    print(sum([p1, p2, Ponto(1, 1)]))              # Ponto(5, 8)
