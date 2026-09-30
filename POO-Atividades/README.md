# POO-Atividades

Material de estudo e atividades de **Programação Orientada a Objetos** (Python), curso de Tecnologia em
Sistemas para Internet, IFRN. Reúne os exemplos das aulas, as listas de exercícios resolvidas e
exercícios extras de treino.

> **Para a prova:** comece pela [`REVISAO.md`](REVISAO.md) (resumo de tudo) e depois use as pastas
> para ver o código completo e executável de cada tópico.

## Como rodar

Requer **Python 3.10+**. Cada pasta é independente:

```bash
cd aulas/06_heranca
python exercicio_gato_cachorro.py
```

Para conferir que tudo executa sem erro: `python rodar_todos.py`.

## Estrutura

```
REVISAO.md        resumo de consulta rápida
aulas/            conteúdo de cada aula (exemplos dos slides + exercícios)
lista_1/          Lista de Exercícios 1 (discursivas nos comentários do arquivo)
lista_2/          Lista de Exercícios 2 (discursivas nos comentários do arquivo)
extras/           treino adicional no formato da AP1
```

### `aulas/`

| Pasta | Aula | Arquivos |
|---|---|---|
| `01_introducao_poo` | POO 07 - Introdução a POO | `carro.py`, `cachorro.py` (exercícios 1 e 2) |
| `02_construtores` | POO 08 - Construtores e métodos de instância | `pessoa_construtor.py`, `conta_bancaria.py`, `circulo_ponto_retangulo.py` (exercícios do livro Pense em Python) |
| `03_metodos_especiais` | E10 - `__str__`, `__repr__`, `__eq__`, `__lt__` | `produto.py`, `tarefa.py`, `conta_eq.py`, `pessoa_lt.py`, `discussao.md` |
| `04_encapsulamento` | POO 09 - Encapsulamento | `pessoa_modificadores.py`, `getters_setters.py`, `cliente.py` |
| `05_excecoes` | E13 - `raise` e exceções personalizadas | `revisao_try_except.py`, `conta_bancaria_erros.py`, `aluno_nota.py`, `estacionamento.py` |
| `06_heranca` | POO 11 - Herança | `heranca_exemplo_01.py`, `exercicio_gato_cachorro.py`, `heranca_multipla.py`, `problema_do_diamante.py` |
| `07_polimorfismo` | POO 12 - Polimorfismo | `polimorfismo_exemplo_01.py`, `injecao_dependencia.py`, `sobrescrita_sobrecarga.py`, `sobrecarga_operadores.py`, `figuras_geometricas.py` (+ `.md` com diagrama UML), `zoologico.py` |
| `08_revisao_ap1` | E15 - Revisão para a AP1 | `livro.py` + `revisao_un02.py` (resolução do problema Biblioteca) e `biblioteca_modelo.py` (versão de referência em um único arquivo) |

### Listas

| Pasta | Lista | Arquivos |
|---|---|---|
| `lista_1` | E08 - Fundamentos | `lista_1.py` (Aluno, Retangulo, Data; discursivas nos comentários) |
| `lista_2` | E14 - Encapsulamento e Exceções | `lista_2.py` (Funcionario, Email; discursivas do Nível 1 nos comentários), `conta_bancaria.py`, `caixa_eletronico.py` |

### `extras/`

`01_estoque.py`, `02_folha_pagamento.py`, `03_template_prova.py` (roteiro de resolução para copiar e adaptar).

## Diferenças em relação aos slides

Alguns exemplos dos slides foram ajustados para funcionar ou fazer mais sentido:

- **Herança (exemplo 1):** no slide, `Cachorro` define `miar()` imprimindo "Au-au"; aqui o método é `latir()`.
- **Herança múltipla:** `Funcionario` ganhou setter de `senha` e `login()` devolve o resultado real da autenticação.
- **Injeção de dependência:** o `Repositorio.select` do slide lança `KeyError` quando o nome não existe;
  aqui usa `dict.get()`.
- **Sobrecarga de operador:** o parâmetro `p3` opcional usa `None` em vez de `Ponto(0, 0)` como padrão
  (evita um objeto compartilhado entre chamadas).
- **Nomes:** métodos em `snake_case` (PEP 8) em vez de `camelCase` (`dizer_nome`, não `dizerNome`).
- Aspas curvas “ ” dos PDFs foram trocadas por aspas retas (as curvas causam `SyntaxError`).
