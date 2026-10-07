class Apartamento:
    def __init__(self, numero: int) -> None:
        self.numero = numero

    def __str__(self) -> str:
        return f"Apartamento {self.numero}"


class Predio:
    def __init__(self, numero_andares: int) -> None:
        self._apartamentos: list[Apartamento] = []

        for andar in range(1, numero_andares + 1):
            apartamento = Apartamento(andar)
            self._apartamentos.append(apartamento)

    def listar_apartamentos(self) -> None:
        for apartamento in self._apartamentos:
            print(apartamento)

print("\nPRÉDIO E APARTAMENTOS")

predio = Predio(5)
predio.listar_apartamentos()


# Predio -> Apartamento: COMPOSIÇÃO.
# O próprio Predio cria os Apartamentos no __init__.