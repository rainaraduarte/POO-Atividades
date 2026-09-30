"""POO 11 - Herança múltipla: o problema do diamante e o MRO.

        ClasseA
        /     \\
   ClasseB   ClasseC     (B e C definem metodo2)
        \\     /
        ClasseD(ClasseC, ClasseB)

Method Resolution Order (MRO): a ordem de busca vai da ESQUERDA para a DIREITA
conforme os pais listados na definição da classe. Veja com ClasseD.__mro__.
"""


class ClasseA:
    def metodo1(self) -> None:
        print("Método 01 - ClasseA")


class ClasseB(ClasseA):
    def metodo2(self) -> None:
        print("Método 02 - ClasseB")


class ClasseC(ClasseA):
    def metodo2(self) -> None:
        print("Método 02 - ClasseC")


class ClasseD(ClasseC, ClasseB):  # C vem ANTES de B
    def metodo3(self) -> None:
        print("Método 03 - ClasseD")


# Variante: trocar a ordem dos pais muda quem "ganha"
class ClasseE(ClasseB, ClasseC):
    pass


if __name__ == "__main__":
    obj = ClasseD()
    obj.metodo1()  # herdado de A
    obj.metodo2()  # ClasseC (C está à esquerda de B)
    obj.metodo3()
    print(ClasseD.__mro__)
    # (D, C, B, A, object)

    ClasseE().metodo2()  # ClasseB
    print(ClasseE.__mro__)
    # (E, B, C, A, object)
