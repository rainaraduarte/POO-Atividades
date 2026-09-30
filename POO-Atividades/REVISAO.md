# Revisão de POO em Python (consulta rápida)

Resumo de tudo que os slides cobrem. Exemplos completos e executáveis estão nas pastas `aulas/`, `lista_1/` e `lista_2/`.

## 1. Classe, objeto, self  (`aulas/01`, `aulas/02`)

```python
class Pessoa:                              # substantivo, inicial maiúscula
    def __init__(self, nome: str, idade: int = 18) -> None:   # construtor (inicializador)
        self.nome = nome                   # atributos NASCEM no __init__
        self.idade = idade

    def dizer_nome(self) -> None:          # 1º parâmetro SEMPRE self
        print(self.nome)

p = Pessoa("Ana")                          # instanciação -> __new__ aloca, __init__ inicializa
p.dizer_nome()                             # o Python passa p como self
```

- Classe = molde; objeto = instância (estado + comportamento + identidade `id()`).
- `b = a` **não copia**: duas referências ao mesmo objeto (`a is b` → `True`).
- `isinstance(obj, Classe)`, `type(obj)`, `hasattr(obj, "attr")`.
- **Nunca** `def __init__(self, notas=[])` (lista padrão é compartilhada entre todos os objetos);
  use `notas=None` e crie a lista dentro. Ou, como na Lista 1: `self.notas = []` no corpo.

## 2. Métodos de classe e estáticos  (`lista_1`)

```python
class Data:
    @classmethod
    def de_texto(cls, txt: str) -> "Data":   # recebe a CLASSE (cls); fábrica alternativa
        d, m, a = txt.split("/")
        return cls(int(d), int(m), int(a))

    @staticmethod
    def bissexto(ano: int) -> bool:          # não recebe self nem cls; utilitário
        return (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0
```

Zeros à esquerda: `f"{dia:02d}/{mes:02d}/{ano}"`. Uma casa decimal: `f"{x:.1f}"`.

## 3. Métodos especiais (dunders)  (`aulas/03`)

| Você escreve | Python chama | Observação |
|---|---|---|
| `print(o)`, `str(o)`, f-string | `__str__` | para **pessoas**; **retorna** str (não imprime) |
| `[o]`, console, depurador | `__repr__` | para **devs**; se só existir `__repr__`, ele também serve ao print |
| `a == b`, `a in lista` | `__eq__` | sem ele, `==` compara **identidade** |
| `sorted`, `min`, `max`, `a < b` | `__lt__` | ou `sorted(x, key=lambda o: o.attr)` |
| `a + b`, `a - b`, `a * k` | `__add__`, `__sub__`, `__mul__` | sobrecarga de operador |
| `sum([...])` | `__radd__` | para começar de `0 + obj` |
| `set`, chave de `dict` | `__hash__` | defina junto com `__eq__` |

```python
def __eq__(self, outro: object) -> bool:
    if not isinstance(outro, Produto):
        return NotImplemented              # deixa o Python tentar o outro lado
    return self.nome == outro.nome         # compare o que IDENTIFICA (não o estado mutável)
```

`!=` é derivado do `__eq__` automaticamente.

## 4. Encapsulamento  (`aulas/04`)

| Sintaxe | Nível | UML |
|---|---|---|
| `nome` | público | `+` |
| `_nome` | protegido (convenção) | `#` |
| `__nome` | privado (name mangling → `_Classe__nome`) | `-` |

```python
class Conta:
    def __init__(self) -> None:
        self._saldo = 0.0                  # protegido

    @property
    def saldo(self) -> float:              # getter -> conta.saldo   (SEM setter = somente leitura)
        return self._saldo

    @saldo.setter                          # só se quiser permitir atribuição
    def saldo(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("saldo negativo")
        self._saldo = valor
```

- Para a validação valer **desde a criação**, faça `self.saldo = saldo` (via setter) no `__init__`.
- `p.total = 10` em property sem setter → `AttributeError`.
- Regra de negócio dentro do método/setter: **um lugar só**.

## 5. Exceções  (`aulas/05`, `lista_2`)

```python
class ErroDeConta(Exception): ...                    # base do domínio
class SaldoInsuficienteError(ErroDeConta): ...       # sufixo Error; corpo pode ser só "..."

def sacar(self, valor):
    if valor > self._saldo:
        raise SaldoInsuficienteError(f"Saldo: {self._saldo:.2f}; pedido: {valor:.2f}")

try:
    conta.sacar(500)
except SaldoInsuficienteError as erro:               # ESPECÍFICO antes do genérico
    print(f"Operação negada: {erro}")
except ErroDeConta as erro:                          # captura pela base
    ...
else:      # roda se NÃO houve exceção
    ...
finally:   # roda SEMPRE
    ...
```

- `raise` > `return False`: o erro não pode ser ignorado sem querer.
- **Nunca** `except:` vazio nem `except Exception: pass`.
- Trate só o que sabe resolver; o resto **propaga**.
- Mensagens com contexto (valores envolvidos).
- Entrada do usuário: `float(input())` pode dar `ValueError`; `float("nan")` e `float("inf")` **passam**
  por `float()`; barre com `math.isfinite`.

## 6. Herança  (`aulas/06`)

```python
class Animal:
    def __init__(self, nome: str, peso: float) -> None:
        self._nome = nome                  # protegido: subclasse acessa
        self._peso = peso

class Gato(Animal):                        # Gato É UM Animal
    def __init__(self, nome: str, peso: float) -> None:
        super().__init__(nome, peso)       # inicializa a parte da superclasse
        self._na_arvore = False
```

- UML: seta de ponta aberta, da subclasse para a superclasse.
- Herança múltipla: `class Gerente(Funcionario, Autenticavel)`; a ordem de busca é o **MRO**
  (esquerda → direita); veja com `Classe.__mro__`.
- Problema do diamante: se B e C definem o mesmo método, vale o do que aparece **primeiro** nos pais.
- `isinstance(g, Animal)` → `True` para subclasses; `issubclass(Gato, Animal)`.

## 7. Polimorfismo  (`aulas/07`)

- **Sobrescrita**: subclasse reescreve o método, **mesma assinatura** (nome + parâmetros).
  `super().metodo()` reaproveita a versão da superclasse.
- **Sobrecarga**: mesmo nome com parâmetros diferentes. Python **não tem** (a última definição vence):
  use parâmetros opcionais (`c=0`), `*args` ou `functools.singledispatchmethod`.
- **Sobrecarga de operador**: `__add__`, `__sub__`, `__eq__`, `__lt__`…
- **Injeção de dependência** (por construtor): a classe **recebe** o colaborador pronto em vez de criá-lo;
  diminui acoplamento e permite trocar por dublê/fake.

```python
class Insersor:
    def __init__(self, repo: Repositorio) -> None:    # injeção
        self._repo = repo
```

- Polimorfismo na prática: `for a in animais: a.moverse()`, sem `if type(a) == ...`.
- `abc.ABC` + `@abstractmethod`: a superclasse define **o quê**, as filhas o **como** (não instancia).

## 8. Conceitos de projeto

- **Coesão**: cada classe cuida de uma responsabilidade. **Acoplamento**: dependência entre classes (evitar).
- **Abstração**: só o essencial ao contexto. **Reuso**: herança e associação.
- Associação/composição: "tem um" (Retângulo **tem** dois Pontos). Herança: "é um".

## 9. Erros que mais penalizam

1. Esquecer `self` na definição do método (`def latir():` → `TypeError`).
2. Atributo criado fora do `__init__`.
3. Validação que "retorna False" e segue a vida (use `raise`).
4. `except` genérico engolindo o erro.
5. `__eq__` sem `isinstance` ou comparando os atributos errados.
6. Aspas curvas “ ” copiadas de slides/PDF → `SyntaxError`. Use `" "` ou `' '`.
7. **Entregar código que não executa**: rode tudo do zero antes de entregar.

## 10. Checklist final

- [ ] Li o enunciado inteiro; listei substantivos (classes/atributos) e verbos (métodos).
- [ ] Type hints e nomes descritivos (PEP 8: `snake_case` em funções/variáveis, `PascalCase` em classes).
- [ ] Estado interno protegido; validação com `raise`.
- [ ] Exceções personalizadas com base comum.
- [ ] Demonstração cobre **sucesso e erro**.
- [ ] Rodei o arquivo do zero (sem erro) nos últimos 10 minutos.

## 11. Perguntas teóricas rápidas

- **Classe × objeto?** Molde × instância.
- **O que é `self`?** O objeto que chamou o método.
- **`_x` × `__x`?** Protegido por convenção × privado com name mangling (`_Classe__x`).
- **`__str__` × `__repr__`?** Legível para o usuário × não ambíguo para o desenvolvedor.
- **Sobrescrita × sobrecarga?** Reescrever na subclasse (mesma assinatura) × mesmo nome com parâmetros
  diferentes (Python emula com opcionais).
- **`@classmethod` × `@staticmethod`?** Recebe `cls` (fábricas) × não recebe nada (utilitário).
- **Por que validar no setter?** Regra em um só lugar; objeto nunca fica inválido.
- **Por que `raise` e não `return False`?** O erro não pode ser ignorado silenciosamente.
- **O que herda `class E(Exception)`?** Todo o comportamento de exceção (lançar, capturar, mensagem).
- **O que é MRO?** Ordem em que o Python procura métodos na herança múltipla.
- **O que é injeção de dependência?** Passar o colaborador pronto (construtor/setter) em vez de a classe criá-lo.
