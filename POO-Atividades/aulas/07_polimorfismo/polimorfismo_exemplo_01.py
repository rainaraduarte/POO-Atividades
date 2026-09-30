"""POO 12 - Polimorfismo: Animal, Gato, Peixe, Passaro.

Mesma mensagem (moverse), comportamentos diferentes: cada subclasse SOBRESCREVE
o método da superclasse mantendo a assinatura.
"""


class Animal:
    def __init__(self) -> None:
        self._posicao = 0

    def moverse(self) -> None:
        pass  # cada subclasse define como


class Gato(Animal):
    def moverse(self) -> None:
        print("Sou um Gato caminhando...")
        self._posicao += 1


class Peixe(Animal):
    def moverse(self) -> None:
        print("Sou um peixe nadando...")
        self._posicao += 1


class Passaro(Animal):
    def moverse(self) -> None:
        print("Sou um pássaro voando...")
        self._posicao += 1


def fazer_mover(animal: Animal) -> None:
    """Quem chama NÃO precisa saber o tipo concreto: só que é um Animal."""
    animal.moverse()


if __name__ == "__main__":
    animais: list[Animal] = [Gato(), Passaro(), Peixe()]
    for animal in animais:
        fazer_mover(animal)  # comportamento depende do objeto real
