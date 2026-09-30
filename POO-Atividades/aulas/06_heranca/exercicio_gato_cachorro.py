"""POO 11 - Exercício: implemente as classes conforme o diagrama UML.

    Animal                        (# = protegido)
      # nome: str
      # peso: float
      # posicao: int
      + moverse(): None
         ^                  ^
    Gato                  Cachorro
      # na_arvore: bool     # qtd_saltos: int
      + miar()              + latir()
      + subir_na_arvore()   + saltar()
      + descer_da_arvore()  + descansar()
      + esta_na_arvore()    + esta_cansado()

Regras do enunciado:
- estaCansado() é True quando o cachorro deu MAIS DO QUE 5 saltos
- estaNaArvore() retorna naArvore; valor padrão: False
- latir e miar escrevem mensagens na tela
- saltar() incrementa qtdSaltos em 1; descansar() decrementa em 1
- construtor de Animal parametriza nome e peso; posição padrão = 0
"""


class Animal:
    def __init__(self, nome: str, peso: float) -> None:
        self._nome = nome
        self._peso = peso
        self._posicao = 0  # padrão: zero

    def moverse(self) -> None:
        self._posicao += 1


class Gato(Animal):
    def __init__(self, nome: str, peso: float) -> None:
        super().__init__(nome, peso)
        self._na_arvore = False  # padrão: fora da árvore

    def miar(self) -> None:
        print(f"{self._nome}: Miau!")

    def subir_na_arvore(self) -> None:
        self._na_arvore = True

    def descer_da_arvore(self) -> None:
        self._na_arvore = False

    def esta_na_arvore(self) -> bool:
        return self._na_arvore


class Cachorro(Animal):
    def __init__(self, nome: str, peso: float) -> None:
        super().__init__(nome, peso)
        self._qtd_saltos = 0

    def latir(self) -> None:
        print(f"{self._nome}: Au au!")

    def saltar(self) -> None:
        self._qtd_saltos += 1

    def descansar(self) -> None:
        # O enunciado só pede "decrementar em 1"; aqui não deixo ficar negativo.
        if self._qtd_saltos > 0:
            self._qtd_saltos -= 1

    def esta_cansado(self) -> bool:
        return self._qtd_saltos > 5  # ESTRITAMENTE maior que 5


if __name__ == "__main__":
    tom = Gato("Tom", 4.2)
    tom.miar()
    print("Na árvore?", tom.esta_na_arvore())   # False (padrão)
    tom.subir_na_arvore()
    print("Na árvore?", tom.esta_na_arvore())   # True
    tom.descer_da_arvore()
    tom.moverse()                               # herdado

    rex = Cachorro("Rex", 12.0)
    rex.latir()
    for _ in range(5):
        rex.saltar()
    print("Cansado com 5 saltos?", rex.esta_cansado())  # False (não é > 5)
    rex.saltar()
    print("Cansado com 6 saltos?", rex.esta_cansado())  # True
    rex.descansar()
    print("Cansado após descansar?", rex.esta_cansado())  # False
