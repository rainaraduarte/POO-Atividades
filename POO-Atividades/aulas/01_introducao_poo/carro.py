"""POO 07 - Exercício 1: abstração de um objeto Carro.

Abstração = isolar só as características essenciais para a aplicação.
Aqui: estado (marca, modelo, cor, ligado, velocidade) e
comportamento (ligar, desligar, acelerar, frear).
"""


class Carro:
    """Molde (classe) a partir do qual criamos objetos Carro."""

    def __init__(self, marca: str, modelo: str, cor: str = "branco") -> None:
        # Atributos = estado do objeto
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ligado = False
        self.velocidade = 0.0

    # Métodos = comportamento do objeto (verbos no infinitivo)
    def ligar(self) -> None:
        if self.ligado:
            print(f"{self.modelo} já está ligado.")
        else:
            self.ligado = True
            print(f"{self.modelo} ligado.")

    def desligar(self) -> None:
        if self.velocidade > 0:
            print("Pare o carro antes de desligar!")
        else:
            self.ligado = False
            print(f"{self.modelo} desligado.")

    def acelerar(self, incremento: float = 10.0) -> None:
        if not self.ligado:
            print("Ligue o carro primeiro.")
            return
        self.velocidade += incremento
        print(f"Velocidade: {self.velocidade:.0f} km/h")

    def frear(self, decremento: float = 10.0) -> None:
        self.velocidade = max(0.0, self.velocidade - decremento)
        print(f"Velocidade: {self.velocidade:.0f} km/h")


if __name__ == "__main__":
    # Programa de teste demonstrativo
    fusca = Carro("Volkswagen", "Fusca", "azul")
    gol = Carro("Volkswagen", "Gol")  # cor padrão

    fusca.acelerar()  # não está ligado
    fusca.ligar()
    fusca.acelerar(30)
    fusca.desligar()  # ainda em movimento
    fusca.frear(50)
    fusca.desligar()

    # Objetos da mesma classe têm os mesmos atributos, mas valores próprios
    print(fusca.cor, gol.cor)
