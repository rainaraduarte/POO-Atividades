"""E10 - Prática 1: dê __str__ e __repr__ a uma classe Tarefa."""


class Tarefa:
    def __init__(self, titulo: str, prazo: str, concluida: bool = False) -> None:
        self.titulo = titulo
        self.prazo = prazo
        self.concluida = concluida

    def concluir(self) -> None:
        self.concluida = True

    def __str__(self) -> str:
        marca = "x" if self.concluida else " "
        return f"[{marca}] {self.titulo} (até {self.prazo})"

    def __repr__(self) -> str:
        return (
            f"Tarefa(titulo={self.titulo!r}, prazo={self.prazo!r}, "
            f"concluida={self.concluida!r})"
        )


if __name__ == "__main__":
    t1 = Tarefa("Estudar POO", "30/09")
    t2 = Tarefa("Entregar lista", "05/10")
    t2.concluir()

    print(t1)             # __str__
    print(t2)
    print(repr(t1))       # __repr__
    print([t1, t2])       # lista mostra o __repr__ dos itens
    print(f"Hoje: {t1}")  # f-string usa __str__
