"""EXTRA (formato AP1) - Controle de Estoque.

Cobre: __init__ validado por property, @classmethod (fábrica), @staticmethod,
__str__/__repr__/__eq__/__lt__, exceções com base comum e programa principal
com fluxos de sucesso e erro.

Enunciado de treino:
- Produto(nome, preco, quantidade); preço e quantidade não podem ser negativos
- Dois produtos são iguais se tiverem o mesmo nome (ignorando maiúsculas)
- Produto.de_texto("Mouse;80.5;10") cria um produto
- Estoque: adicionar(produto), retirar(nome, qtd), valor_total(), abaixo_do_minimo(limite)
- Retirar mais do que existe -> EstoqueInsuficienteError;
  nome inexistente -> ProdutoNaoEncontradoError
"""


class ErroDeEstoque(Exception):
    """Base dos erros do domínio de estoque."""


class ProdutoNaoEncontradoError(ErroDeEstoque):
    pass


class EstoqueInsuficienteError(ErroDeEstoque):
    pass


class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int = 0) -> None:
        self.nome = nome
        self.preco = preco            # setter valida
        self.quantidade = quantidade  # setter valida

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, valor: float) -> None:
        if valor < 0:
            raise ValueError(f"Preço negativo: {valor}")
        self.__preco = float(valor)

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, valor: int) -> None:
        if valor < 0:
            raise ValueError(f"Quantidade negativa: {valor}")
        self.__quantidade = int(valor)

    @classmethod
    def de_texto(cls, texto: str) -> "Produto":
        nome, preco, qtd = texto.split(";")
        return cls(nome.strip(), float(preco), int(qtd))

    @staticmethod
    def formatar_moeda(valor: float) -> str:
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    def subtotal(self) -> float:
        return self.preco * self.quantidade

    def __str__(self) -> str:
        return f"{self.nome}: {self.quantidade} un. x {self.formatar_moeda(self.preco)}"

    def __repr__(self) -> str:
        return f"Produto({self.nome!r}, {self.preco!r}, {self.quantidade!r})"

    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, Produto):
            return NotImplemented
        return self.nome.lower() == outro.nome.lower()

    def __hash__(self) -> int:
        return hash(self.nome.lower())

    def __lt__(self, outro: "Produto") -> bool:
        return self.nome.lower() < outro.nome.lower()


class Estoque:
    def __init__(self) -> None:
        self._produtos: list[Produto] = []

    def adicionar(self, produto: Produto) -> None:
        if produto in self._produtos:  # usa o __eq__
            existente = self._buscar(produto.nome)
            existente.quantidade += produto.quantidade
        else:
            self._produtos.append(produto)

    def _buscar(self, nome: str) -> Produto:
        for p in self._produtos:
            if p.nome.lower() == nome.lower():
                return p
        raise ProdutoNaoEncontradoError(nome)

    def retirar(self, nome: str, qtd: int) -> None:
        produto = self._buscar(nome)
        if qtd > produto.quantidade:
            raise EstoqueInsuficienteError(
                f"{nome}: pedido {qtd}, disponível {produto.quantidade}"
            )
        produto.quantidade -= qtd

    def valor_total(self) -> float:
        return sum(p.subtotal() for p in self._produtos)

    def abaixo_do_minimo(self, limite: int) -> list[Produto]:
        return sorted(p for p in self._produtos if p.quantidade < limite)


if __name__ == "__main__":
    est = Estoque()
    est.adicionar(Produto.de_texto("Mouse;80.5;10"))
    est.adicionar(Produto("Teclado", 120, 3))
    est.adicionar(Produto("mouse", 80.5, 5))  # mesmo nome -> soma a quantidade

    est.retirar("Teclado", 1)
    print(*sorted(est._produtos), sep="\n")
    print("Total:", Produto.formatar_moeda(est.valor_total()))
    print("Abaixo de 5:", est.abaixo_do_minimo(5))

    for nome, qtd in (("Teclado", 50), ("Monitor", 1)):
        try:
            est.retirar(nome, qtd)
        except EstoqueInsuficienteError as erro:
            print("Estoque insuficiente:", erro)
        except ErroDeEstoque as erro:
            print(f"{type(erro).__name__}: {erro}")

    try:
        Produto("Cabo", -5)
    except ValueError as erro:
        print("Inválido:", erro)
