"""E10 - Prática 2: __eq__ em ContaBancaria (iguais se tiverem o mesmo número)."""


class ContaBancaria:
    def __init__(self, numero: str, titular: str, saldo: float = 0.0) -> None:
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, ContaBancaria):
            return NotImplemented
        return self.numero == outro.numero  # identidade da conta = número

    def __hash__(self) -> int:
        return hash(self.numero)  # coerente com __eq__

    def __repr__(self) -> str:
        return f"ContaBancaria({self.numero!r}, {self.titular!r}, saldo={self.saldo})"


if __name__ == "__main__":
    c1 = ContaBancaria("123-4", "Ana", 100.0)
    c2 = ContaBancaria("123-4", "Ana", 5000.0)  # mesmo número, saldo diferente
    c3 = ContaBancaria("999-9", "Ana", 100.0)   # mesmo saldo, número diferente

    print(c1 == c2)        # True  -> mesma conta, só o estado mudou
    print(c1 == c3)        # False -> contas diferentes
    print(c1 in [c2, c3])  # True
    print(len({c1, c2, c3}))  # 2 (set usa __hash__ + __eq__)
