"""E15 - Revisão AP1: problema-modelo "Biblioteca" (formato da avaliação).

Enunciado:
- Livro(titulo, ano, disponivel) e Biblioteca (acervo interno)
- Biblioteca: cadastrar(livro), emprestar(titulo), devolver(titulo), disponiveis()
- Emprestar livro indisponível -> LivroIndisponivelError;
  título inexistente -> LivroNaoEncontradoError
- Dois livros são iguais se tiverem mesmo título e ano
- Programa principal demonstrando os fluxos de sucesso e de erro

Método de resolução (checklist do professor):
1. ler o enunciado inteiro; 2. listar substantivos (classes/atributos) e verbos
(métodos); 3. implementar incrementalmente: classe -> testa -> próxima;
4. reservar 10 min finais para rodar tudo do zero.
"""


# ----------------------------------------------------------------- Exceções
class ErroDeBiblioteca(Exception):
    """Base comum: permite capturar qualquer erro do domínio."""


class LivroIndisponivelError(ErroDeBiblioteca):
    """Livro já está emprestado."""


class LivroNaoEncontradoError(ErroDeBiblioteca):
    """Título não existe no acervo."""


# -------------------------------------------------------------------- Livro
class Livro:
    def __init__(self, titulo: str, ano: int) -> None:
        # Estado nasce COMPLETO e válido no __init__
        self.titulo = titulo
        self.ano = ano
        self.disponivel = True

    def __str__(self) -> str:
        status = "disponível" if self.disponivel else "emprestado"
        return f"{self.titulo} ({self.ano}) - {status}"

    def __repr__(self) -> str:
        return f"Livro(titulo={self.titulo!r}, ano={self.ano!r})"

    def __eq__(self, outro: object) -> bool:
        # Regra do enunciado: mesmo título E mesmo ano (não olha disponibilidade!)
        if not isinstance(outro, Livro):
            return NotImplemented
        return self.titulo == outro.titulo and self.ano == outro.ano

    def __hash__(self) -> int:
        return hash((self.titulo, self.ano))


# --------------------------------------------------------------- Biblioteca
class Biblioteca:
    def __init__(self) -> None:
        self._acervo: list[Livro] = []  # protegido: só a classe mexe

    def cadastrar(self, livro: Livro) -> None:
        self._acervo.append(livro)

    def _buscar(self, titulo: str) -> Livro:
        """Apoio interno, reutilizado por emprestar e devolver."""
        for livro in self._acervo:
            if livro.titulo == titulo:
                return livro
        raise LivroNaoEncontradoError(titulo)

    def emprestar(self, titulo: str) -> None:
        livro = self._buscar(titulo)
        if not livro.disponivel:  # regra de negócio DENTRO da Biblioteca
            raise LivroIndisponivelError(titulo)
        livro.disponivel = False

    def devolver(self, titulo: str) -> None:
        self._buscar(titulo).disponivel = True

    def disponiveis(self) -> list[Livro]:
        return [livro for livro in self._acervo if livro.disponivel]


if __name__ == "__main__":
    biblio = Biblioteca()
    biblio.cadastrar(Livro("Dom Casmurro", 1899))
    biblio.cadastrar(Livro("Memórias Póstumas", 1881))
    biblio.cadastrar(Livro("Quincas Borba", 1891))

    # Fluxo de SUCESSO
    biblio.emprestar("Dom Casmurro")
    print("Disponíveis:", *biblio.disponiveis(), sep="\n  ")
    biblio.devolver("Dom Casmurro")
    print("Após devolução:", len(biblio.disponiveis()), "disponíveis")

    # Fluxos de ERRO (captura pela base: qualquer erro do domínio)
    for titulo in ("Quincas Borba", "Quincas Borba", "Ulisses"):
        try:
            biblio.emprestar(titulo)
            print(f"Emprestado: {titulo}")
        except LivroIndisponivelError as erro:
            print(f"Operação negada (indisponível): {erro}")
        except ErroDeBiblioteca as erro:
            print(f"Operação negada ({type(erro).__name__}): {erro}")

    # __eq__ pela regra do enunciado
    print(Livro("A", 2000) == Livro("A", 2000))  # True
    print(Livro("A", 2000) == Livro("A", 2001))  # False
