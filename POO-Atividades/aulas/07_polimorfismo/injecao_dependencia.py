"""POO 12 - Injeção de Dependência (por construtor) + sobrescrita.

Insersor NÃO cria o seu Repositorio: recebe um pronto (injeção). Isso reduz o
acoplamento e permite trocar por um repositório FALSO nos testes.

Correção em relação ao slide: o select original faz
`self.__baseDeDados[nome]`, que lança KeyError quando o nome não existe.
Aqui usamos .get(), que devolve None nesse caso.
"""


class Repositorio:
    def __init__(self) -> None:
        self.__base_de_dados: dict[str, int] = {}

    def select(self, nome: str) -> str | None:
        idade = self.__base_de_dados.get(nome)
        if idade is not None:
            return f"{nome}, {idade}"
        return None

    def insert(self, nome: str, idade: int) -> str:
        self.__base_de_dados[nome] = idade
        return f"Inserindo dados: {nome} e {idade}"


class Insersor:
    def __init__(self, repo: Repositorio) -> None:  # injeção por construtor
        self.__repositorio = repo

    def inserir_dado(self, nome: str, idade: int) -> str:
        if self.__repositorio.select(nome):
            return "Dado já existe no repositório"
        return self.__repositorio.insert(nome, idade)


class RepoFalsoSelectVazio(Repositorio):
    """Dublê: select SEMPRE diz que não existe (sobrescrita do select)."""

    def select(self, nome: str) -> str | None:
        return None


class RepoFalsoSelectTrue(Repositorio):
    """Dublê: select SEMPRE diz que já existe."""

    def select(self, nome: str) -> str | None:
        return "existe"


if __name__ == "__main__":
    # Repositório real
    insersor = Insersor(Repositorio())
    print(insersor.inserir_dado("Ana", 20))   # Inserindo dados...
    print(insersor.inserir_dado("Ana", 20))   # Dado já existe...

    # Testando só a lógica do Insersor com dublês (sem base real)
    print(Insersor(RepoFalsoSelectVazio()).inserir_dado("dado", 1))  # insere
    print(Insersor(RepoFalsoSelectTrue()).inserir_dado("dado", 1))   # já existe
