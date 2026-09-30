"""Lista de Exercícios 1 - Fundamentos (E08) - Prof. Higor Morais.

Contém o Nível 2 (questões 6 a 9). As questões discursivas da Lista 1
estão respondidas nos comentários logo abaixo.

Critérios da entrega: funcionamento, type hints, nomes, uso correto de
self e dos dunders. (Na entrega original: um arquivo com todas as questões,
cada uma indicada por comentário.)
"""

# =============================================================================
# QUESTÕES DISCURSIVAS - LISTA 1 (com respostas)
# =============================================================================
#
# 1) Qual a diferença entre classe e objeto? Dê um exemplo com código
#
#    Classe é o molde: descreve os atributos (estado) e os métodos
#    (comportamento) que os objetos terão. Objeto é a INSTÂNCIA: a
#    materialização da classe em tempo de execução, com valores próprios e
#    identidade própria (id). De uma classe saem vários objetos.
#
#        class Cachorro:                      # classe (molde)
#            def __init__(self, nome: str) -> None:
#                self.nome = nome
#
#            def latir(self) -> None:
#                print(f"{self.nome}: Au!")
#
#        rex = Cachorro("Rex")                # objeto (instância)
#        mel = Cachorro("Mel")                # outro objeto da mesma classe
#        rex.latir()                          # Rex: Au!
#
# 2) O que o self representa dentro de um método?
#
#    É a referência ao PRÓPRIO OBJETO que chamou o método. Em rex.latir(), o
#    Python passa rex automaticamente como primeiro parâmetro (self). É por ele
#    que o método acessa self.nome, self.saldo etc. do objeto certo. O nome
#    "self" é convenção, mas o primeiro parâmetro é sempre o objeto.
#
# 3) O que acontece na memória em: a = Conta(); b = a
#
#    Só UM objeto Conta é criado (na primeira linha). "b = a" NÃO copia o
#    objeto: cria uma segunda referência (outro nome) para o MESMO objeto.
#
#        a = Conta()
#        b = a
#        print(a is b)          # True
#        print(id(a) == id(b))  # True
#        b.saldo = 100
#        print(a.saldo)         # 100 -> mexer por b altera "a": é o mesmo objeto
#
#    Para dois objetos independentes seria preciso instanciar de novo
#    (b = Conta()) ou copiar (copy.copy).
#
# 4) Sem executar: o que imprime print(p) se a classe de p não define __str__?
#
#    A representação padrão herdada de object: nome da classe + endereço de
#    memória, algo como:
#
#        <__main__.Pessoa object at 0x7f2c1a3b5d90>
#
#    Solução: definir __str__ (para pessoas) e/ou __repr__ (para desenvolvedores).
#
# 5) Aponte o erro:
#
#        class Cachorro():
#            def latir():
#                print("Au!")
#
#        rex = Cachorro()
#        rex.latir()
#
#    O método latir NÃO recebe self. Ao chamar rex.latir(), o Python passa o
#    objeto como primeiro argumento automaticamente, mas o método não declara
#    parâmetro nenhum:
#
#        TypeError: Cachorro.latir() takes 0 positional arguments but 1 was given
#
#    Correção: def latir(self):
#    (Obs.: no PDF as aspas de "Au!" são curvas; ao copiar dá SyntaxError.
#    Use aspas retas.)
# =============================================================================



# ---------------------------------------------------------------- Questão 6
class Aluno:
    """Aluno com lista interna de notas, iniciada vazia."""

    def __init__(self, nome: str, matricula: str) -> None:
        self.nome = nome
        self.matricula = matricula
        self.notas: list[float] = []  # cada aluno tem a SUA lista

    def lancar_nota(self, valor: float) -> None:
        self.notas.append(valor)

    def media(self) -> float:
        if not self.notas:  # evita ZeroDivisionError
            return 0.0
        return sum(self.notas) / len(self.notas)

    def aprovado(self) -> bool:
        return self.media() >= 6

    def __str__(self) -> str:
        # Formato pedido: "Ana (20261234) — média 7.5"
        return f"{self.nome} ({self.matricula}) — média {self.media():.1f}"


# ---------------------------------------------------------------- Questão 8
class Retangulo:
    def __init__(self, base: float, altura: float) -> None:
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)

    def __eq__(self, outro: object) -> bool:
        """Iguais se tiverem as mesmas dimensões."""
        if not isinstance(outro, Retangulo):
            return NotImplemented
        return self.base == outro.base and self.altura == outro.altura

    def __hash__(self) -> int:
        return hash((self.base, self.altura))


# ---------------------------------------------------------------- Questão 9
class Data:
    def __init__(self, dia: int, mes: int, ano: int) -> None:
        self.dia = dia
        self.mes = mes
        self.ano = ano

    @classmethod
    def de_texto(cls, texto: str) -> "Data":
        """Fábrica alternativa: Data.de_texto("09/08/2026")."""
        dia, mes, ano = texto.split("/")
        return cls(int(dia), int(mes), int(ano))

    @staticmethod
    def bissexto(ano: int) -> bool:
        """Não usa self nem cls: é uma função utilitária ligada à classe."""
        return (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0

    def __str__(self) -> str:
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano}"


if __name__ == "__main__":
    # ------------------------------------------------------------ Questão 7
    print("# Questão 7")
    ana = Aluno("Ana", "20261234")
    bruno = Aluno("Bruno", "20265678")
    carla = Aluno("Carla", "20269012")

    for nota in (8.0, 7.0):
        ana.lancar_nota(nota)
    for nota in (4.0, 5.5):
        bruno.lancar_nota(nota)
    for nota in (6.0, 6.0, 9.0):
        carla.lancar_nota(nota)

    print(ana)  # Ana (20261234) — média 7.5
    for aluno in (ana, bruno, carla):
        if aluno.aprovado():
            print("Aprovado:", aluno)

    # ------------------------------------------------------------ Questão 8
    print("# Questão 8")
    r1 = Retangulo(3, 4)
    r2 = Retangulo(3, 4)
    r3 = Retangulo(4, 3)
    print(r1.area(), r1.perimetro())  # 12 14
    print(r1 == r2)                   # True  (mesmas dimensões)
    print(r1 == r3)                   # False (dimensões trocadas)
    print(r1 is r2)                   # False

    # ------------------------------------------------------------ Questão 9
    print("# Questão 9")
    d = Data.de_texto("09/08/2026")
    print(d)                          # 09/08/2026
    print(Data(1, 2, 2027))           # 01/02/2027
    print(Data.bissexto(2024), Data.bissexto(1900), Data.bissexto(2000))
    # True False True
