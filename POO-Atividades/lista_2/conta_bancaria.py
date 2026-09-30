"""Lista 2 - Questão 9 (Nível 3): ContaBancaria completa.

- _saldo protegido + property saldo SOMENTE leitura
- depositar e sacar
- Exceções: ValorInvalidoError, SaldoInsuficienteError, LimiteExcedidoError,
  todas filhas de ErroDeConta
- Limite de saque por operação: R$ 1.000
"""

import math


class ErroDeConta(Exception):
    """Base de todos os erros do domínio de contas."""


class ValorInvalidoError(ErroDeConta):
    """Valor não numérico, não finito ou não positivo."""


class SaldoInsuficienteError(ErroDeConta):
    """Saque maior que o saldo."""


class LimiteExcedidoError(ErroDeConta):
    """Saque acima do limite por operação."""


class ContaBancaria:
    LIMITE_SAQUE = 1000.0

    def __init__(self, titular: str) -> None:
        self.titular = titular
        self._saldo = 0.0

    @property
    def saldo(self) -> float:
        """Somente leitura: sem setter, `conta.saldo = 10` dá AttributeError."""
        return self._saldo

    @staticmethod
    def _validar_valor(valor: float) -> None:
        # math.isfinite barra nan e inf, que passam por float() e por `<= 0`
        if not math.isfinite(valor) or valor <= 0:
            raise ValorInvalidoError(f"Valor inválido: {valor}")

    def depositar(self, valor: float) -> None:
        self._validar_valor(valor)
        self._saldo += valor

    def sacar(self, valor: float) -> None:
        self._validar_valor(valor)
        if valor > self.LIMITE_SAQUE:
            raise LimiteExcedidoError(
                f"Limite por saque: R$ {self.LIMITE_SAQUE:.2f}; pedido: R$ {valor:.2f}"
            )
        if valor > self._saldo:
            raise SaldoInsuficienteError(
                f"Saldo: R$ {self._saldo:.2f}; pedido: R$ {valor:.2f}"
            )
        self._saldo -= valor


if __name__ == "__main__":
    conta = ContaBancaria("Maria")
    conta.depositar(3000)

    casos = [
        ("sacar", 200),
        ("sacar", 1500),          # LimiteExcedidoError
        ("sacar", -5),            # ValorInvalidoError
        ("depositar", 0),         # ValorInvalidoError
        ("depositar", float("nan")),  # ValorInvalidoError
        ("sacar", 1000),          # no limite: permitido
        ("sacar", 5000),          # LimiteExcedidoError (checado antes do saldo)
    ]
    for operacao, valor in casos:
        try:
            getattr(conta, operacao)(valor)
            print(f"{operacao}({valor}) ok -> saldo R$ {conta.saldo:.2f}")
        except ErroDeConta as erro:
            print(f"{operacao}({valor}) -> {type(erro).__name__}: {erro}")

    try:
        conta.saldo = 1_000_000  # type: ignore[misc]
    except AttributeError as erro:
        print("saldo é somente leitura:", erro)

    conta2 = ContaBancaria("João")
    try:
        conta2.sacar(50)
    except ErroDeConta as erro:
        print(f"{type(erro).__name__}: {erro}")  # SaldoInsuficienteError
