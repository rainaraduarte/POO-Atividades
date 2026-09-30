"""E13 - Prática: ContaBancaria com exceções do domínio.

- ErroDeConta: base comum (permite capturar "qualquer erro de conta")
- SaldoInsuficienteError e ValorInvalidoError: filhas de ErroDeConta
- raise em vez de "return False": o erro não pode ser ignorado em silêncio
"""


class ErroDeConta(Exception):
    """Base para todos os erros do domínio de contas."""


class SaldoInsuficienteError(ErroDeConta):
    """Saque maior que o saldo disponível."""


class ValorInvalidoError(ErroDeConta):
    """Valor de operação não positivo."""


class ContaBancaria:
    def __init__(self, titular: str) -> None:
        self.titular = titular
        self._saldo = 0.0

    @property
    def saldo(self) -> float:
        return self._saldo

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValorInvalidoError(f"Depósito inválido: {valor:.2f}")
        self._saldo += valor

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            raise ValorInvalidoError(f"Saque inválido: {valor:.2f}")
        if valor > self._saldo:
            raise SaldoInsuficienteError(
                f"Saldo: {self._saldo:.2f}; pedido: {valor:.2f}"
            )
        self._saldo -= valor


if __name__ == "__main__":
    conta = ContaBancaria("Maria")
    conta.depositar(300)

    # except específico é MELHOR que except genérico
    try:
        conta.sacar(500.0)
    except SaldoInsuficienteError as erro:
        print(f"Operação negada: {erro}")

    try:
        conta.depositar(-10)
    except ValorInvalidoError as erro:
        print(f"Operação negada: {erro}")

    # Desafio: capturar pela BASE qualquer erro do domínio
    for operacao, valor in (("sacar", 0), ("sacar", 999), ("depositar", 50)):
        try:
            getattr(conta, operacao)(valor)
            print(f"{operacao}({valor}) ok -> saldo {conta.saldo:.2f}")
        except ErroDeConta as erro:
            print(f"{operacao}({valor}) falhou ({type(erro).__name__}): {erro}")
