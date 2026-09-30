"""E10 - Prática 3: __lt__ em Pessoa (por idade) e ordenação com sorted."""


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def __lt__(self, outro: "Pessoa") -> bool:
        return self.idade < outro.idade

    def __str__(self) -> str:
        return f"{self.nome} ({self.idade} anos)"


if __name__ == "__main__":
    pessoas = [Pessoa("Carlos", 42), Pessoa("Ana", 19), Pessoa("Bia", 30)]

    for p in sorted(pessoas):                 # crescente por idade
        print(p)
    print("Mais nova:", min(pessoas))
    print("Mais velha:", max(pessoas))
    for p in sorted(pessoas, reverse=True):   # decrescente
        print(p)

    # Ordenar por outro critério SEM mudar a classe:
    for p in sorted(pessoas, key=lambda p: p.nome):
        print(p)
