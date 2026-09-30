"""POO 12 - Exercício 1: figuras geométricas Círculo e Retângulo (2D).

Requisitos do enunciado:
- toda FiguraGeometrica sabe calcular área e perímetro (polimorfismo);
- Ponto: atributos x e y;
- Retangulo: dois Pontos (canto superior esquerdo e canto inferior direito);
- Circulo: um Ponto (centro) e raio;
- usar polimorfismo, sobrescrita de método e sobrecarga de operador;
- diagrama de classes: ver figuras_geometricas.md;
- demonstração do funcionamento.
"""

import math
from abc import ABC, abstractmethod


class Ponto:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    # Sobrecarga de operadores
    def __add__(self, outro: "Ponto") -> "Ponto":
        return Ponto(self.x + outro.x, self.y + outro.y)

    def __sub__(self, outro: "Ponto") -> "Ponto":
        return Ponto(self.x - outro.x, self.y - outro.y)

    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, Ponto):
            return NotImplemented
        return self.x == outro.x and self.y == outro.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def distancia(self, outro: "Ponto") -> float:
        return math.hypot(self.x - outro.x, self.y - outro.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


class FiguraGeometrica(ABC):
    """Superclasse: define O QUE toda figura sabe fazer, não COMO."""

    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimetro(self) -> float: ...

    # Sobrecarga de operadores de comparação: figuras se ordenam por área
    def __lt__(self, outra: "FiguraGeometrica") -> bool:
        return self.area() < outra.area()

    def __eq__(self, outra: object) -> bool:
        if not isinstance(outra, FiguraGeometrica):
            return NotImplemented
        return type(self) is type(outra) and self.area() == outra.area()

    def __hash__(self) -> int:
        return hash((type(self).__name__, self.area()))

    def __str__(self) -> str:
        return (
            f"{type(self).__name__}: área={self.area():.2f}, "
            f"perímetro={self.perimetro():.2f}"
        )


class Retangulo(FiguraGeometrica):
    def __init__(self, canto_sup_esq: Ponto, canto_inf_dir: Ponto) -> None:
        self.canto_sup_esq = canto_sup_esq
        self.canto_inf_dir = canto_inf_dir

    @property
    def largura(self) -> float:
        return abs(self.canto_inf_dir.x - self.canto_sup_esq.x)

    @property
    def altura(self) -> float:
        return abs(self.canto_inf_dir.y - self.canto_sup_esq.y)

    def area(self) -> float:  # sobrescrita
        return self.largura * self.altura

    def perimetro(self) -> float:  # sobrescrita
        return 2 * (self.largura + self.altura)


class Circulo(FiguraGeometrica):
    def __init__(self, centro: Ponto, raio: float) -> None:
        if raio <= 0:
            raise ValueError("O raio deve ser positivo.")
        self.centro = centro
        self.raio = raio

    def area(self) -> float:  # sobrescrita
        return math.pi * self.raio**2

    def perimetro(self) -> float:  # sobrescrita
        return 2 * math.pi * self.raio


if __name__ == "__main__":
    ret = Retangulo(Ponto(0, 4), Ponto(3, 0))   # 3 x 4
    cir = Circulo(Ponto(1, 1), 2)
    quad = Retangulo(Ponto(0, 2), Ponto(2, 0))  # 2 x 2

    figuras: list[FiguraGeometrica] = [ret, cir, quad]

    for figura in figuras:  # POLIMORFISMO: mesmo código, cálculo de cada classe
        print(figura)

    print("Ordenadas por área:")
    for figura in sorted(figuras):
        print(" ", figura)

    print("Maior:", max(figuras))
    print("Soma das áreas: %.2f" % sum(f.area() for f in figuras))

    # Operadores de Ponto
    a, b = Ponto(1, 2), Ponto(3, 5)
    print(a + b, b - a, a == Ponto(1, 2))

    try:
        FiguraGeometrica()  # type: ignore[abstract]
    except TypeError as erro:
        print("Classe abstrata não instancia:", erro)
