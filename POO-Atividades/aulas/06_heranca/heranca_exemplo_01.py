"""POO 11 - Exemplo 1: Animal, Gato e Cachorro (herança simples).

Herança = relacionamento "É UM": um gato É UM animal.
Em UML: seta com ponta aberta e linha contínua, da subclasse para a superclasse.

Obs.: no slide a classe Cachorro define miar() imprimindo "Au-au...";
aqui o método se chama latir(), que é o que faz sentido (e o que o exercício pede).
"""


class Animal:
    def __init__(self, nome: str, peso: float) -> None:
        self._nome = nome      # protegido: subclasses podem acessar
        self._peso = peso
        self._posicao = 0

    def moverse(self) -> None:
        self._posicao += 1


class Gato(Animal):
    def __init__(self, nome: str, peso: float) -> None:
        super().__init__(nome, peso)  # chama o __init__ da superclasse

    def miar(self) -> None:
        print("Miau...")

    def __str__(self) -> str:
        return f"Gato: {self._nome}; Peso: {self._peso}; Posição: {self._posicao}"


class Cachorro(Animal):
    def __init__(self, nome: str, peso: float) -> None:
        super().__init__(nome, peso)

    def latir(self) -> None:
        print("Au-au...")

    def __str__(self) -> str:
        return f"Cachorro: {self._nome}; Peso: {self._peso}; Posição: {self._posicao}"


if __name__ == "__main__":
    gato = Gato("Tom", 2)
    cachorro = Cachorro("Pluto", 4)

    gato.miar()
    gato.moverse()        # método HERDADO de Animal
    cachorro.latir()
    cachorro.moverse()
    gato.miar()
    gato.moverse()
    gato.moverse()

    print(gato)           # Posição: 3
    print(cachorro)       # Posição: 1

    print(isinstance(gato, Gato), isinstance(gato, Animal), isinstance(gato, Cachorro))
    # True True False
    print(issubclass(Gato, Animal))  # True
