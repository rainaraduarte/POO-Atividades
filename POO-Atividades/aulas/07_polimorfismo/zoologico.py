"""POO 12 - Exercício 2: sistema de um zoológico.

O zoológico tem vários animais; todos podem se movimentar, emitir som e têm
um custo de alimentação. Animais especializados diferenciam-se por sobrescrita
de métodos (polimorfismo).
"""


class Animal:
    CUSTO_POR_KG = 1.0  # R$ por kg do animal por dia (cada espécie sobrescreve)

    def __init__(self, nome: str, peso: float) -> None:
        self._nome = nome
        self._peso = peso

    @property
    def nome(self) -> str:
        return self._nome

    def emitir_som(self) -> str:
        return "..."

    def mover_se(self) -> str:
        return f"{self._nome} se move."

    def custo_alimentacao(self) -> float:
        return self._peso * self.CUSTO_POR_KG

    def __str__(self) -> str:
        return f"{type(self).__name__} {self._nome} ({self._peso:.0f} kg)"


class Leao(Animal):
    CUSTO_POR_KG = 0.20  # carne

    def emitir_som(self) -> str:
        return "Roaaar!"

    def mover_se(self) -> str:
        return f"{self._nome} caminha majestosamente."


class Macaco(Animal):
    CUSTO_POR_KG = 0.50

    def emitir_som(self) -> str:
        return "Uh uh ah ah!"

    def mover_se(self) -> str:
        return f"{self._nome} pula de galho em galho."


class Elefante(Animal):
    CUSTO_POR_KG = 0.02

    def emitir_som(self) -> str:
        return "Pruuuu!"

    def mover_se(self) -> str:
        return f"{self._nome} marcha pesadamente."


class Cobra(Animal):
    CUSTO_POR_KG = 0.05

    def emitir_som(self) -> str:
        return "Sssss!"

    def mover_se(self) -> str:
        return f"{self._nome} rasteja."


class Zoologico:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self._animais: list[Animal] = []

    def adicionar(self, animal: Animal) -> None:
        self._animais.append(animal)

    def custo_total(self) -> float:
        return sum(a.custo_alimentacao() for a in self._animais)

    def visita_guiada(self) -> None:
        print(f"== {self.nome} ==")
        for animal in self._animais:  # polimorfismo: não checa o tipo
            print(f"{animal}: {animal.emitir_som()} | {animal.mover_se()}")


if __name__ == "__main__":
    zoo = Zoologico("Zoo IFRN")
    zoo.adicionar(Leao("Simba", 190))
    zoo.adicionar(Macaco("Caco", 12))
    zoo.adicionar(Elefante("Dumbo", 4000))
    zoo.adicionar(Cobra("Nagini", 30))

    zoo.visita_guiada()
    print(f"Custo diário de alimentação: R$ {zoo.custo_total():.2f}")
