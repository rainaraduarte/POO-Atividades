"""POO 08 - __new__ / __init__, parâmetros padrão e o erro de aridade."""


class Pessoa:
    """__init__ sem valores padrão: os dois argumentos são obrigatórios."""

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade


class Pessoa2:
    """idade tem valor padrão; nome continua obrigatório."""

    def __init__(self, nome: str, idade: int = 18) -> None:
        self.nome = nome
        self.idade = idade


class Pessoa3:
    """Todos os parâmetros têm padrão: Pessoa3() é válido."""

    def __init__(self, nome: str = "Maria", idade: int = 18) -> None:
        self.nome = nome
        self.idade = idade


if __name__ == "__main__":
    p1 = Pessoa("Fulano", 20)
    p2 = Pessoa2("Cicrana")          # idade = 18
    p3 = Pessoa3()                   # nome = "Maria", idade = 18
    print(f"Meu nome é {p1.nome} tenho {p1.idade} anos")
    print(f"Meu nome é {p2.nome} tenho {p2.idade} anos")
    print(f"Meu nome é {p3.nome} tenho {p3.idade} anos")

    # O slide mostra que Pessoa2() dá erro: nome é obrigatório.
    try:
        Pessoa2()  # type: ignore[call-arg]
    except TypeError as erro:
        print("TypeError:", erro)
