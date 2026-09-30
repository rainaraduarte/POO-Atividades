# Diagrama de classes - Figuras geométricas

```mermaid
classDiagram
    class Ponto {
        +float x
        +float y
        +__add__(outro) Ponto
        +__sub__(outro) Ponto
        +__eq__(outro) bool
        +distancia(outro) float
    }
    class FiguraGeometrica {
        <<abstract>>
        +area() float
        +perimetro() float
        +__lt__(outra) bool
    }
    class Retangulo {
        +Ponto canto_sup_esq
        +Ponto canto_inf_dir
        +area() float
        +perimetro() float
    }
    class Circulo {
        +Ponto centro
        +float raio
        +area() float
        +perimetro() float
    }
    FiguraGeometrica <|-- Retangulo : é um
    FiguraGeometrica <|-- Circulo : é um
    Retangulo o-- Ponto : 2 pontos
    Circulo o-- Ponto : centro
```

Legenda UML: `+` público, `#` protegido, `-` privado; `<|--` herança (seta de ponta
aberta da subclasse para a superclasse); `o--` associação/agregação.
