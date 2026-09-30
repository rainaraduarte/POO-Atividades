"""POO 08 - Métodos de instância: a classe ContaBancaria dos slides.

Também mostra type(), isinstance() e hasattr().
"""


class ContaBancaria:
    def __init__(self, numero: str, agencia: str) -> None:
        self.numero = numero
        self.agencia = agencia
        self.saldo = 0.0

    def depositar(self, valor: float) -> None:
        self.saldo += valor

    def sacar(self, valor: float) -> bool:
        """Retorna True se sacou, False se saldo insuficiente.

        (Depois de Exceções, o ideal é lançar erro em vez de retornar False.)
        """
        if self.saldo < valor:
            return False
        self.saldo -= valor
        return True


if __name__ == "__main__":
    c1 = ContaBancaria("12345", "33-4")
    c1.depositar(500)
    print(c1.sacar(200))  # True
    print(c1.sacar(900))  # False
    print(c1.saldo)       # 300.0

    if isinstance(c1, ContaBancaria):
        print(type(c1))   # <class '__main__.ContaBancaria'>
    print(hasattr(c1, "saldo"), hasattr(c1, "limite"))  # True False
