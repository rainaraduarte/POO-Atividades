"""EXTRA - Folha de pagamento: herança + polimorfismo + property + exceções.

Enunciado de treino:
- Funcionario(nome, salario_base): salário não pode ser <= 0
- calcular_pagamento() é polimórfico:
    Gerente        -> salário + 20% de bônus
    Desenvolvedor  -> salário + horas_extras * 50
    Estagiario     -> valor fixo da bolsa (ignora o salário_base)
- Folha recebe a lista de funcionários (injeção por construtor) e calcula
  o total e a lista ordenada por pagamento.
"""


class FuncionarioInvalidoError(Exception):
    pass


class Funcionario:
    def __init__(self, nome: str, salario_base: float) -> None:
        self.nome = nome
        self.salario_base = salario_base

    @property
    def salario_base(self) -> float:
        return self._salario_base

    @salario_base.setter
    def salario_base(self, valor: float) -> None:
        if valor <= 0:
            raise FuncionarioInvalidoError(f"Salário inválido para {self.nome}: {valor}")
        self._salario_base = float(valor)

    def calcular_pagamento(self) -> float:
        return self._salario_base

    def __str__(self) -> str:
        return f"{type(self).__name__} {self.nome}: R$ {self.calcular_pagamento():.2f}"

    def __lt__(self, outro: "Funcionario") -> bool:
        return self.calcular_pagamento() < outro.calcular_pagamento()


class Gerente(Funcionario):
    def calcular_pagamento(self) -> float:
        return super().calcular_pagamento() * 1.20  # reaproveita a superclasse


class Desenvolvedor(Funcionario):
    VALOR_HORA_EXTRA = 50.0

    def __init__(self, nome: str, salario_base: float, horas_extras: int = 0) -> None:
        super().__init__(nome, salario_base)
        self.horas_extras = horas_extras

    def calcular_pagamento(self) -> float:
        return super().calcular_pagamento() + self.horas_extras * self.VALOR_HORA_EXTRA


class Estagiario(Funcionario):
    BOLSA = 1200.0

    def __init__(self, nome: str) -> None:
        super().__init__(nome, self.BOLSA)

    def calcular_pagamento(self) -> float:
        return self.BOLSA


class Folha:
    def __init__(self, funcionarios: list[Funcionario]) -> None:  # injeção
        self._funcionarios = funcionarios

    def total(self) -> float:
        return sum(f.calcular_pagamento() for f in self._funcionarios)

    def ranking(self) -> list[Funcionario]:
        return sorted(self._funcionarios, reverse=True)  # usa __lt__


if __name__ == "__main__":
    equipe: list[Funcionario] = [
        Gerente("Marta", 8000),
        Desenvolvedor("Caio", 5000, horas_extras=10),
        Estagiario("Duda"),
    ]
    folha = Folha(equipe)
    for f in folha.ranking():
        print(f)
    print(f"Total da folha: R$ {folha.total():.2f}")

    try:
        Desenvolvedor("Zé", 0)
    except FuncionarioInvalidoError as erro:
        print("Erro:", erro)
