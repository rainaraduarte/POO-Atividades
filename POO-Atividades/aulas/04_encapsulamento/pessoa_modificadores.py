"""POO 09 - Modificadores de acesso em Python (por convenção de nomes).

    nome     -> público     (UML: +)
    _idade   -> protegido   (UML: #)  convenção: "não mexa de fora"
    __cpf    -> privado     (UML: -)  name mangling: vira _Pessoa__cpf

Python não bloqueia de verdade: é convenção + ofuscação de nome.
"""


class Pessoa:
    def __init__(self, nome: str, idade: int = 20, cep: str | None = None) -> None:
        self.nome = nome        # público
        self._idade = idade     # protegido (convenção)
        self.__cep = cep        # privado (name mangling)

    def dizer_nome(self) -> None:
        print(f"Meu nome é {self.nome}")

    def atualizar_cep(self, cep: str) -> None:
        # A regra de negócio fica DENTRO do método (encapsulada)
        if len(cep) != 8:
            print("Quantidade de dígitos inválida!")
        else:
            self.__cep = cep
            print("CEP atualizado com sucesso!")

    def is_adulto(self) -> bool:
        return self._idade >= 18


if __name__ == "__main__":
    p1 = Pessoa("Fulano")

    print([a for a in dir(p1) if not a.startswith("__")])
    # ['_Pessoa__cep', '_idade', 'atualizar_cep', 'dizer_nome', 'is_adulto', 'nome']

    print(p1.nome)             # ok, público
    print(p1._idade)           # funciona, mas é convenção não usar de fora
    # print(p1.__cep)          # AttributeError: name mangling
    print(p1._Pessoa__cep)     # None -> acesso "forçado": _NomeDaClasse__atributo

    p1.atualizar_cep("123")        # inválido
    p1.atualizar_cep("59162000")   # válido
    print(p1._Pessoa__cep)
    print(p1.is_adulto())
