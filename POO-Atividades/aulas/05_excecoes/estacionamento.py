"""E13 - Prática: Estacionamento(vagas) e EstacionamentoLotadoError.

entrar() lança EstacionamentoLotadoError quando cheio; o programa principal
trata o erro e informa o usuário.
"""


class EstacionamentoLotadoError(Exception):
    """Não há vagas disponíveis."""


class Estacionamento:
    def __init__(self, vagas: int) -> None:
        if vagas <= 0:
            raise ValueError("O estacionamento precisa ter ao menos 1 vaga.")
        self._vagas = vagas
        self._ocupadas = 0

    @property
    def vagas_livres(self) -> int:
        return self._vagas - self._ocupadas

    def entrar(self) -> None:
        if self._ocupadas >= self._vagas:
            raise EstacionamentoLotadoError(
                f"Estacionamento lotado ({self._vagas} vagas)."
            )
        self._ocupadas += 1

    def sair(self) -> None:
        if self._ocupadas == 0:
            raise ValueError("Não há carros para sair.")
        self._ocupadas -= 1


def main() -> None:
    estac = Estacionamento(2)

    for carro in range(1, 4):
        try:
            estac.entrar()
            print(f"Carro {carro} entrou. Vagas livres: {estac.vagas_livres}")
        except EstacionamentoLotadoError as erro:
            print(f"Carro {carro} não pôde entrar: {erro}")

    estac.sair()
    print(f"Um carro saiu. Vagas livres: {estac.vagas_livres}")


if __name__ == "__main__":
    main()
