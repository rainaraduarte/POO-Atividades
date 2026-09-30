"""POO 12 - Sobrescrita (override) x Sobrecarga (overload) de métodos.

SOBRESCRITA: subclasse reescreve método da superclasse, MESMA assinatura.
SOBRECARGA : vários métodos com o mesmo nome e parâmetros diferentes.
             Python NÃO tem sobrecarga "de verdade" (tipagem dinâmica; a última
             definição vence). Alternativas: parâmetros opcionais, *args e
             (extra, fora dos slides) functools.singledispatchmethod.
"""

from functools import singledispatchmethod


# ------------------------------------------------------------------ Sobrescrita
class Funcionario:
    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario

    def bonus(self) -> float:
        return self.salario * 0.05


class Gerente(Funcionario):
    def bonus(self) -> float:  # mesma assinatura: sobrescrita
        return self.salario * 0.20

    def bonus_com_base(self) -> float:
        # super() reaproveita a versão da superclasse
        return super().bonus() + 500


# ------------------------------------------------------------------ Sobrecarga
class Calculadora:
    # Em Python, a ÚLTIMA definição substitui a anterior:
    def soma_ruim(self, a: int, b: int) -> int:
        return a + b

    def soma_ruim(self, a: int, b: int, c: int) -> int:  # noqa: F811
        return a + b + c

    # Jeito Pythônico 1: parâmetro opcional
    def soma(self, a: float, b: float, c: float = 0) -> float:
        return a + b + c

    # Jeito Pythônico 2: quantidade variável de argumentos
    def soma_todos(self, *valores: float) -> float:
        return sum(valores)


class Descritor:
    """Sobrecarga por TIPO do argumento (extra): singledispatchmethod."""

    @singledispatchmethod
    def descrever(self, valor: object) -> str:
        return f"objeto: {valor}"

    @descrever.register
    def _(self, valor: int) -> str:
        return f"inteiro: {valor}"

    @descrever.register
    def _(self, valor: str) -> str:
        return f"texto: {valor!r}"


if __name__ == "__main__":
    f = Funcionario("Ana", 3000)
    g = Gerente("Bruno", 3000)
    print(f.bonus(), g.bonus(), g.bonus_com_base())  # 150.0 600.0 650.0

    calc = Calculadora()
    try:
        calc.soma_ruim(1, 2)  # só existe a versão de 3 parâmetros
    except TypeError as erro:
        print("TypeError:", erro)
    print(calc.soma(1, 2), calc.soma(1, 2, 3))
    print(calc.soma_todos(1, 2, 3, 4, 5))

    d = Descritor()
    print(d.descrever(10), "|", d.descrever("oi"), "|", d.descrever(3.5))
