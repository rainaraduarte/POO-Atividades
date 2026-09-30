"""E10 - Métodos especiais: __str__, __repr__, __eq__, __lt__ (classe Produto).

Quem CHAMA os dunders é a linguagem; nós só os definimos.
    print(obj)      -> obj.__str__()
    a == b          -> a.__eq__(b)
    sorted(lista)   -> usa __lt__
"""


class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco

    def __str__(self) -> str:
        """Versão para PESSOAS (print, str(), f-string)."""
        return f"{self.nome} (R$ {self.preco:.2f})"

    def __repr__(self) -> str:
        """Versão para DESENVOLVEDORES (console, depurador, dentro de listas)."""
        return f"Produto(nome={self.nome!r}, preco={self.preco!r})"

    def __eq__(self, outro: object) -> bool:
        """Igualdade por VALOR (sem isto, == compara identidade, como `is`)."""
        if not isinstance(outro, Produto):
            return NotImplemented  # deixa o Python tentar o outro lado
        return self.nome == outro.nome and self.preco == outro.preco

    def __lt__(self, outro: "Produto") -> bool:
        """Ordem natural: por preço. Habilita sorted, min e max."""
        return self.preco < outro.preco

    # Ao definir __eq__, o Python remove o __hash__ automático. Se o objeto
    # precisar ir em set ou ser chave de dict, defina __hash__ coerente:
    def __hash__(self) -> int:
        return hash((self.nome, self.preco))


if __name__ == "__main__":
    a = Produto("Teclado", 120.0)
    b = Produto("Teclado", 120.0)

    print(a)               # Teclado (R$ 120.00)   -> __str__
    print(f"Item: {a}")    # f-string também usa __str__
    print(repr(a))         # Produto(nome='Teclado', preco=120.0)
    print([a])             # listas usam o __repr__ dos itens

    print(a == b)          # True  (por valor)
    print(a is b)          # False (identidades diferentes)
    print(a != b)          # False (__ne__ é derivado do __eq__)
    print(a in [b])        # True
    print(a == "Teclado")  # False (NotImplemented -> Python devolve False)

    itens = [Produto("Mouse", 80.0), Produto("Teclado", 120.0), Produto("Cabo", 25.0)]
    for p in sorted(itens):
        print(p)           # Cabo, Mouse, Teclado
    print(min(itens), max(itens))

    # Alternativa sem __lt__: key=
    print(sorted(itens, key=lambda p: p.nome))
