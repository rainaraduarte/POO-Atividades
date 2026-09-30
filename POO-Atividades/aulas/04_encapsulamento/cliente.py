"""POO 09 - Exercício de fixação: classe Cliente a partir do diagrama UML.

    Cliente
    - nome: str
    - cpf: str
    - renda: float

Construtor com TODOS os atributos, getters/setters via @property e
testes de validação.
"""


class Cliente:
    def __init__(self, nome: str, cpf: str, renda: float) -> None:
        # Passa pelos setters -> a validação vale desde a criação do objeto
        self.nome = nome
        self.cpf = cpf
        self.renda = renda

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        if not nome.strip():
            raise ValueError("O nome não pode ser vazio.")
        self.__nome = nome.strip()

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str) -> None:
        digitos = "".join(c for c in cpf if c.isdigit())
        if len(digitos) != 11:
            raise ValueError("O CPF deve ter 11 dígitos.")
        self.__cpf = digitos

    @property
    def renda(self) -> float:
        return self.__renda

    @renda.setter
    def renda(self, renda: float) -> None:
        if renda < 0:
            raise ValueError("A renda não pode ser negativa.")
        self.__renda = float(renda)

    def __str__(self) -> str:
        return f"{self.nome} - CPF {self.cpf} - renda R$ {self.renda:.2f}"


if __name__ == "__main__":
    c = Cliente("Maria Silva", "123.456.789-09", 3500)
    print(c)

    c.renda = 4000            # setter (válido)
    print(c.renda)

    # Testes de validação
    testes = [
        ("renda negativa", lambda: setattr(c, "renda", -1)),
        ("CPF curto", lambda: setattr(c, "cpf", "123")),
        ("nome vazio", lambda: setattr(c, "nome", "   ")),
        ("criação inválida", lambda: Cliente("", "12345678909", 10)),
    ]
    for descricao, acao in testes:
        try:
            acao()
        except ValueError as erro:
            print(f"[{descricao}] recusado: {erro}")

    print(c)  # continua consistente após as tentativas inválidas
