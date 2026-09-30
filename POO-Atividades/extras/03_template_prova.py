"""TEMPLATE para resolver problemas de modelagem em prova (copie e adapte).

Passo a passo:
 1. Leia o enunciado INTEIRO antes da primeira linha.
 2. Sublinhe SUBSTANTIVOS (classes/atributos) e VERBOS (métodos).
 3. Anote as REGRAS (validações, quem é igual a quem, ordenação).
 4. Implemente incrementalmente: exceções -> classe simples -> teste -> próxima.
 5. Rode a demonstração (sucesso E erro). Código que não roda perde quase tudo.
"""

# ------------------------------------------------------------ 1) Exceções
class ErroDoDominio(Exception):
    """Base comum: uma classe por tipo de erro, todas filhas desta."""


class RegraVioladaError(ErroDoDominio):
    pass


# ------------------------------------------------------------ 2) Entidade
class Entidade:
    def __init__(self, nome: str, valor: float) -> None:
        self.nome = nome    # atributos "públicos" que passam por property
        self.valor = valor  # -> a validação vale já na criação

    @property
    def valor(self) -> float:
        return self.__valor

    @valor.setter
    def valor(self, novo: float) -> None:
        if novo < 0:
            raise RegraVioladaError(f"Valor negativo: {novo}")
        self.__valor = novo

    @classmethod
    def de_texto(cls, texto: str) -> "Entidade":
        nome, valor = texto.split(";")
        return cls(nome, float(valor))

    def __str__(self) -> str:
        return f"{self.nome}: {self.valor:.2f}"

    def __repr__(self) -> str:
        return f"Entidade({self.nome!r}, {self.valor!r})"

    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, Entidade):
            return NotImplemented
        return self.nome == outro.nome  # <- o que IDENTIFICA a entidade

    def __hash__(self) -> int:
        return hash(self.nome)

    def __lt__(self, outro: "Entidade") -> bool:
        return self.valor < outro.valor


# ------------------------------------------------------------ 3) Serviço
class Repositorio:
    def __init__(self) -> None:
        self._itens: list[Entidade] = []  # estado interno protegido

    def adicionar(self, item: Entidade) -> None:
        self._itens.append(item)

    def listar(self) -> list[Entidade]:
        return sorted(self._itens)


# ------------------------------------------------------------ 4) Demonstração
if __name__ == "__main__":
    repo = Repositorio()
    repo.adicionar(Entidade("a", 10))
    repo.adicionar(Entidade.de_texto("b;5"))
    print(*repo.listar(), sep="\n")

    try:
        Entidade("ruim", -1)
    except ErroDoDominio as erro:  # captura pela base
        print("Erro de domínio:", erro)
