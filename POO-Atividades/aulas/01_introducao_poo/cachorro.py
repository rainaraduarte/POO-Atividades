"""POO 07 - Exercício 2: abstração de um objeto Cachorro.

Também demonstra os três pilares de um objeto: estado, comportamento
e identidade (id), e a diferença entre igualdade de valor e identidade.
"""


class Cachorro:
    def __init__(self, nome: str, raca: str, energia: int = 10) -> None:
        self.nome = nome
        self.raca = raca
        self.energia = energia

    def latir(self) -> None:
        print(f"{self.nome}: Au au!")

    def correr(self) -> None:
        if self.energia < 3:  # correr custa 3 de energia
            print(f"{self.nome} está cansado demais.")
            return
        self.energia -= 3
        print(f"{self.nome} correu. Energia: {self.energia}")

    def comer(self) -> None:
        self.energia += 5
        print(f"{self.nome} comeu. Energia: {self.energia}")

    def dizer_nome(self) -> None:
        # self.<atributo> acessa o atributo DO OBJETO que chamou o método
        print(f"Meu nome é {self.nome}")


if __name__ == "__main__":
    rex = Cachorro("Rex", "Vira-lata")
    toto = Cachorro("Totó", "Poodle", energia=5)

    rex.latir()
    rex.correr()
    toto.correr()
    toto.correr()  # energia acaba
    toto.comer()

    # Estado, identidade e referências
    outro_rex = Cachorro("Rex", "Vira-lata")
    mesmo_rex = rex  # NÃO cria objeto novo: só outra referência

    print(rex.nome == outro_rex.nome)  # True  (mesmo valor de atributo)
    print(id(rex) == id(outro_rex))    # False (identidades diferentes)
    print(id(rex) == id(mesmo_rex))    # True  (mesmo objeto)
    print(rex is mesmo_rex)            # True

    mesmo_rex.nome = "Rex II"          # altera o MESMO objeto
    print(rex.nome)                    # Rex II
