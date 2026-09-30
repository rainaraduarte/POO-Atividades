"""POO 09 - Getters e setters: estilo clássico x @property (Pythônico)."""


# ------------------------------------------------- 1) Estilo clássico (Java-like)
class PessoaClassica:
    def __init__(self, nome: str, cpf: str) -> None:
        self.__nome = nome
        self.__cpf = cpf

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str) -> None:
        self.__nome = nome

    def get_cpf(self) -> str:
        return self.__cpf

    def set_cpf(self, cpf: str) -> None:
        self.__cpf = cpf


# ------------------------------------------------- 2) Com o decorator @property
class Pessoa:
    def __init__(self, nome: str, cpf: str) -> None:
        self.__nome = nome
        self.__cpf = cpf

    @property
    def nome(self) -> str:          # getter: p.nome
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:  # setter: p.nome = "..."
        self.__nome = nome

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str) -> None:
        self.__cpf = cpf


if __name__ == "__main__":
    p = PessoaClassica("Jose", "123.456.789-00")
    print(f"Meu nome é {p.get_nome()}")
    p.set_cpf("111.222.333-44")
    print(f"Meu novo CPF é {p.get_cpf()}")

    # Com property, a chamada parece acesso a atributo público,
    # mas a lógica continua encapsulada nos métodos.
    q = Pessoa("Jose", "123.456.789-00")
    print(f"Meu nome é {q.nome}")
    q.cpf = "111.222.333-44"
    print(f"Meu novo CPF é {q.cpf}")
