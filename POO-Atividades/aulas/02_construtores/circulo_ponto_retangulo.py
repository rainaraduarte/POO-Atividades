"""POO 08 - Exercícios do livro Pense em Python (Downey), cap. 15-16.

1. Classe Circle com center (Point) e radius.
2. Instanciar Circle com centro (150, 100) e raio 75.
3. point_in_circle(circle, point)
4. rect_in_circle(circle, rect)
5. rect_circle_overlap(circle, rect)  (+ versão desafiadora)

Convenção: Rectangle.corner é o canto INFERIOR ESQUERDO; width e height
crescem para a direita (x) e para cima (y).
"""

import math


class Point:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


class Rectangle:
    def __init__(self, corner: Point, width: float, height: float) -> None:
        self.corner = corner  # canto inferior esquerdo
        self.width = width
        self.height = height

    def corners(self) -> list[Point]:
        x, y = self.corner.x, self.corner.y
        return [
            Point(x, y),
            Point(x + self.width, y),
            Point(x, y + self.height),
            Point(x + self.width, y + self.height),
        ]


class Circle:
    def __init__(self, center: Point, radius: float) -> None:
        self.center = center
        self.radius = radius


def distance_between_points(p1: Point, p2: Point) -> float:
    return math.hypot(p1.x - p2.x, p1.y - p2.y)


def point_in_circle(circle: Circle, point: Point) -> bool:
    """True se o ponto está dentro ou no limite do círculo."""
    return distance_between_points(circle.center, point) <= circle.radius


def rect_in_circle(circle: Circle, rect: Rectangle) -> bool:
    """True se o retângulo está TOTALMENTE dentro (ou no limite) do círculo.

    Basta os quatro cantos estarem dentro: o círculo é convexo.
    """
    return all(point_in_circle(circle, canto) for canto in rect.corners())


def rect_circle_overlap(circle: Circle, rect: Rectangle) -> bool:
    """Versão simples: True se ALGUM canto do retângulo cai dentro do círculo."""
    return any(point_in_circle(circle, canto) for canto in rect.corners())


def rect_circle_overlap_full(circle: Circle, rect: Rectangle) -> bool:
    """Versão desafiadora: True se QUALQUER parte do retângulo toca o círculo.

    Acha o ponto do retângulo mais próximo do centro (clamp) e testa a
    distância até ele.
    """
    x_min, y_min = rect.corner.x, rect.corner.y
    x_max, y_max = x_min + rect.width, y_min + rect.height
    mais_proximo = Point(
        min(max(circle.center.x, x_min), x_max),
        min(max(circle.center.y, y_min), y_max),
    )
    return point_in_circle(circle, mais_proximo)


if __name__ == "__main__":
    # Exercício 2
    circulo = Circle(Point(150, 100), 75)

    print(point_in_circle(circulo, Point(150, 100)))  # True  (centro)
    print(point_in_circle(circulo, Point(225, 100)))  # True  (no limite)
    print(point_in_circle(circulo, Point(300, 300)))  # False

    dentro = Rectangle(Point(130, 80), 40, 40)
    fora = Rectangle(Point(400, 400), 10, 10)
    # só o canto inferior esquerdo (200, 90) está dentro do círculo
    cruzando = Rectangle(Point(200, 90), 100, 20)

    print(rect_in_circle(circulo, dentro))              # True
    print(rect_in_circle(circulo, cruzando))            # False
    print(rect_circle_overlap(circulo, cruzando))       # True (canto (200,90))
    print(rect_circle_overlap(circulo, fora))           # False

    # Caso em que NENHUM canto está dentro, mas o retângulo cruza o círculo
    faixa = Rectangle(Point(0, 95), 300, 10)
    print(rect_circle_overlap(circulo, faixa))          # False (só cantos)
    print(rect_circle_overlap_full(circulo, faixa))     # True  (versão completa)
