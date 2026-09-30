"""E13 - Prática: no setter da nota do Aluno, trocar o retorno silencioso
por raise ValueError com mensagem clara.

Antes (ruim): se a nota fosse inválida, o setter só dava `return` e o erro sumia.
Depois (bom): a violação da regra interrompe a operação e explica o motivo.
"""


class Aluno:
    def __init__(self, nome: str, nota: float = 0.0) -> None:
        self.nome = nome
        self.nota = nota  # passa pelo setter: valida já na criação

    @property
    def nota(self) -> float:
        return self.__nota

    @nota.setter
    def nota(self, valor: float) -> None:
        if not 0 <= valor <= 10:
            raise ValueError(f"Nota inválida: {valor}. Use um valor entre 0 e 10.")
        self.__nota = float(valor)


if __name__ == "__main__":
    aluno = Aluno("Ana", 7.5)
    print(aluno.nome, aluno.nota)

    for valor in (9, 11, -1):
        try:
            aluno.nota = valor
            print("nota atualizada para", aluno.nota)
        except ValueError as erro:
            print("Erro:", erro)

    try:
        Aluno("Bia", 15)
    except ValueError as erro:
        print("Erro na criação:", erro)
