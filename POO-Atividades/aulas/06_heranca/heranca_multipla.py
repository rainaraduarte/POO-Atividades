"""POO 11 - Herança múltipla: Funcionario, Autenticavel, Gerente, Diretor, Cliente.

Autenticavel é um "mixin": oferece uma funcionalidade comum (autenticar) a
classes sem parentesco entre si. Gerente e Diretor herdam DUAS classes.

Ajustes em relação ao slide:
- Funcionario ganhou setter de senha (senão nunca haveria senha para testar);
- login() devolve o resultado real da autenticação.
"""


class Funcionario:
    def __init__(self, nome: str, matricula: str) -> None:
        self.__nome = nome
        self.__matricula = matricula
        self.__senha = ""

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def senha(self) -> str:
        return self.__senha

    @senha.setter
    def senha(self, senha: str) -> None:
        self.__senha = senha


class Autenticavel:
    def autenticar(self, senha: str) -> bool:
        # self é o objeto que chamou; self.senha usa a property DELE
        if self.senha == senha:  # type: ignore[attr-defined]
            print("Autenticado!")
            return True
        print("Senha incorreta.")
        return False


class Gerente(Funcionario, Autenticavel):
    def __init__(self, nome: str, matricula: str) -> None:
        super().__init__(nome, matricula)  # __init__ de Funcionario


class Diretor(Funcionario, Autenticavel):
    def __init__(self, nome: str, matricula: str) -> None:
        super().__init__(nome, matricula)

    def emitir_relatorio(self) -> None:
        print("Emitindo relatório...")


class Cliente(Autenticavel):
    def __init__(self, nome: str) -> None:
        super().__init__()
        self.__nome = nome
        self.__senha = ""

    @property
    def senha(self) -> str:
        return self.__senha

    @senha.setter
    def senha(self, senha: str) -> None:
        self.__senha = senha


class Pessoa:
    """Não é Autenticavel."""


class SistemaBancario:
    def login(self, obj: object, senha: str) -> bool:
        if hasattr(obj, "autenticar"):  # "duck typing": tem o método? então serve
            return obj.autenticar(senha)  # type: ignore[attr-defined]
        print(f"{obj.__class__.__name__} não é autenticável")
        return False


if __name__ == "__main__":
    sistema = SistemaBancario()

    diretor = Diretor("João", "22333")
    gerente = Gerente("Maria", "44555")
    cliente = Cliente("Ana")
    pessoa = Pessoa()

    diretor.senha = "d123"
    gerente.senha = "g456"
    cliente.senha = "c789"

    print(sistema.login(diretor, "d123"))   # True
    print(sistema.login(gerente, "errada")) # False
    print(sistema.login(cliente, "c789"))   # True
    print(sistema.login(pessoa, "x"))       # False (não autenticável)

    diretor.emitir_relatorio()

    print(Gerente.__mro__)
    print(isinstance(gerente, Funcionario), isinstance(gerente, Autenticavel))
