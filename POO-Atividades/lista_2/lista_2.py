"""Lista de Exercícios 2 - Encapsulamento e Exceções (E14) - Nível 2.

Questões 6, 7 e 8. As questões 9 e 10 (Nível 3) estão em conta_bancaria.py
e caixa_eletronico.py. O Nível 1 está respondido nos comentários logo abaixo.
"""

# =============================================================================
# QUESTÕES DISCURSIVAS - LISTA 2, NÍVEL 1 (com respostas)
# =============================================================================
#
# 1) Qual a diferença prática entre _saldo e __saldo? O que é name mangling?
#
#    _saldo (um underline) é protegido por CONVENÇÃO: continua acessível de
#    fora (obj._saldo), mas o programador avisa "não mexa aqui". Subclasses
#    podem usar normalmente.
#    __saldo (dois underlines) é privado: o Python RENOMEIA o atributo
#    internamente para _NomeDaClasse__saldo. Isso é o name mangling (name
#    decoration): o nome fica "ofuscado" para não ser acessado por engano de
#    fora nem colidir com o de subclasses.
#    Não é segurança real: obj._Conta__saldo ainda funciona.
#
#        class Conta:
#            def __init__(self):
#                self._saldo = 0      # protegido
#                self.__senha = "x"   # privado -> _Conta__senha
#
#        c = Conta()
#        print(c._saldo)         # 0 (funciona, mas não é boa prática)
#        # print(c.__senha)      # AttributeError
#        print(c._Conta__senha)  # x
#
# 2) Sem executar: o que acontece em p.total = 10 se total é uma property
#    sem setter?
#
#    Lança AttributeError (property sem setter é SOMENTE LEITURA):
#    "AttributeError: property 'total' of 'X' object has no setter".
#
# 3) Por que validar no setter é melhor do que validar em cada ponto que usa
#    o atributo?
#
#    - A regra fica em UM único lugar (encapsulamento): mudou a regra, muda um
#      método só.
#    - Não dá para "esquecer" de validar em algum ponto do código.
#    - Vale desde a criação do objeto, se o __init__ passar pelo setter.
#    - O objeto nunca fica em estado inválido, e quem usa a classe não precisa
#      conhecer a regra.
#
# 4) Aponte o problema: except Exception: pass
#
#    O erro é ENGOLIDO em silêncio: captura qualquer exceção (genérica demais,
#    inclusive bugs imprevistos) e não faz nada. O programa segue com estado
#    possivelmente corrompido e ninguém fica sabendo. É o bug mais caro de
#    encontrar. Correto: capturar a exceção ESPECÍFICA que se sabe resolver,
#    tratar/informar, e deixar as demais PROPAGAREM.
#
# 5) O que herda quem escreve class MeuErro(Exception)?
#
#    Herda de Exception toda a maquinaria de exceção: pode ser lançada com
#    raise, capturada com except MeuErro, guarda a mensagem (str(erro),
#    erro.args) e também é capturada por except Exception. Como toda exceção é
#    um OBJETO de uma classe, criar a sua é só herdar; o corpo pode ser apenas
#    a docstring.
# =============================================================================



# ------------------------------------------------------------ Exceções
class SalarioInvalidoError(Exception):
    """Salário abaixo do mínimo."""


class EmailInvalidoError(Exception):
    """E-mail sem '@' ou sem '.'."""


# ---------------------------------------------------------- Questão 6
class Funcionario:
    SALARIO_MINIMO = 1621.00  # 2026 (Decreto 12.797/2025) - ajuste se o enunciado pedir outro

    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario  # usa o setter -> valida na criação

    @property
    def salario(self) -> float:
        return self._salario

    @salario.setter
    def salario(self, valor: float) -> None:
        if valor < self.SALARIO_MINIMO:
            raise SalarioInvalidoError(
                f"Salário R$ {valor:.2f} abaixo do mínimo "
                f"(R$ {self.SALARIO_MINIMO:.2f})."
            )
        self._salario = float(valor)

    def aumentar(self, percentual: float) -> None:
        """Aceita apenas 0 < percentual <= 30, senão ValueError."""
        if not 0 < percentual <= 30:
            raise ValueError(
                f"Percentual inválido: {percentual}. Use 0 < percentual <= 30."
            )
        self._salario *= 1 + percentual / 100


# ---------------------------------------------------------- Questão 7
class Email:
    def __init__(self, endereco: str) -> None:
        self.endereco = endereco  # passa pelo setter

    @property
    def endereco(self) -> str:
        return self._endereco

    @endereco.setter
    def endereco(self, valor: str) -> None:
        if "@" not in valor or "." not in valor:
            raise EmailInvalidoError(f"E-mail inválido: {valor!r}")
        self._endereco = valor

    def __str__(self) -> str:
        return self._endereco


if __name__ == "__main__":
    # ------------------------------------------------------ Questão 8
    print("# Funcionario")
    f = Funcionario("Ana", 2000)
    f.aumentar(10)
    print(f"{f.nome}: R$ {f.salario:.2f}")  # 2200.00

    try:  # erro 1: salário abaixo do mínimo
        Funcionario("Bruno", 1000)
    except SalarioInvalidoError as erro:
        print("Erro:", erro)

    try:  # erro 2: percentual fora da faixa
        f.aumentar(50)
    except ValueError as erro:
        print("Erro:", erro)

    print("# Email")
    e = Email("ana@ifrn.edu.br")
    print(e)

    for teste in ("anaifrn.edu.br", "ana@ifrn"):  # sem '@' / sem '.'
        try:
            Email(teste)
        except EmailInvalidoError as erro:
            print("Erro:", erro)
