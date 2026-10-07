class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco

    def __str__(self) -> str:
        return f"{self.nome} - R$ {self.preco:.2f}"


class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int) -> None:
        self.produto = produto
        self.quantidade = quantidade

    @property
    def subtotal(self) -> float:
        return self.produto.preco * self.quantidade

    def __str__(self) -> str:
        return (
            f"{self.quantidade}x {self.produto.nome} "
            f": R$ {self.subtotal:.2f}"
        )


class Pedido:
    def __init__(self, cliente: "Cliente") -> None:
        self.cliente = cliente

        self._itens: list[ItemPedido] = []

    def adicionar(self, produto: Produto, quantidade: int) -> None:
        item = ItemPedido(produto, quantidade)
        self._itens.append(item)

    @property
    def total(self) -> float:
        return sum(item.subtotal for item in self._itens)

    def __str__(self) -> str:
        linhas = "\n".join(f"- {item}" for item in self._itens)

        return (
            f"Pedido de {self.cliente.nome}\n"
            f"{linhas}\n"
            f"Total: R$ {self.total:.2f}"
        )


class Cliente:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self._pedidos: list[Pedido] = []

    def fazer_pedido(self) -> Pedido:
        pedido = Pedido(self)
        self._pedidos.append(pedido)
        return pedido


print("SISTEMA DE PEDIDOS")

cliente = Cliente("Hanna")

hamburguer = Produto("Hambúrguer", 15.00)
refrigerante = Produto("Refrigerante", 6.00)

pedido = cliente.fazer_pedido()

pedido.adicionar(hamburguer, 2)
pedido.adicionar(refrigerante, 1)

print(pedido)


# Cliente -> Pedido: ASSOCIAÇÃO.
# O Cliente conhece seus pedidos e o Pedido referencia o Cliente.
# O Pedido não é uma parte criada dentro do Cliente no sentido de composição.
# Pedido -> ItemPedido: COMPOSIÇÃO. O Pedido cria seus ItemPedido dentro do método adicionar().
# O ItemPedido é uma parte exclusiva do Pedido.
# ItemPedido -> Produto: AGREGAÇÃO. O Produto pode existir independentemente do ItemPedido. ele é criado fora e depois entregue ao ItemPedido.
