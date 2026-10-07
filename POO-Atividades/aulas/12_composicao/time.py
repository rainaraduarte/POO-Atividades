class Jogador:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.time = None

    def __str__(self) -> str:
        if self.time:
            return f"{self.nome} - {self.time.nome}"
        return f"{self.nome} - Sem time"


class Time:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self._jogadores: list[Jogador] = []

    def adicionar_jogador(self, jogador: Jogador) -> None:
        if jogador not in self._jogadores:
            self._jogadores.append(jogador)
            jogador.time = self

    def remover_jogador(self, jogador: Jogador) -> None:
        if jogador in self._jogadores:
            self._jogadores.remove(jogador)
            jogador.time = None

    def listar_jogadores(self) -> None:
        for jogador in self._jogadores:
            print(jogador.nome)



print("\nTIME E JOGADOR")

jogador = Jogador("José")

time_a = Time("Time A")
time_b = Time("Time B")

time_a.adicionar_jogador(jogador)
print(jogador)

time_a.remover_jogador(jogador)
time_b.adicionar_jogador(jogador)

print(jogador)


# Time -> Jogador: AGREGAÇÃO.
# O Jogador existe independentemente do Time e pode trocar de time.