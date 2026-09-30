# Discussão (E10): por que comparar contas pelo número e não pelo saldo?

- O **saldo** é *estado*: muda a cada depósito ou saque. Se `==` usasse o saldo,
  a mesma conta seria "diferente de si mesma" depois de um depósito.
- O **número** é a *identidade de negócio* da conta: não muda durante a vida do
  objeto. Duas variáveis com o mesmo número representam **a mesma conta**.
- Isso separa três ideias que costumam se misturar:
  - `is` → é literalmente o mesmo objeto na memória (identidade da linguagem).
  - `==` sem `__eq__` → o mesmo que `is`.
  - `==` com `__eq__` → **nós** decidimos o que torna dois objetos "iguais"
    (decisão de modelagem).
- Regra prática: compare pelos atributos que **identificam** a entidade e que
  **não mudam**; nunca pelos que representam estado mutável.
- Se definir `__eq__`, defina também `__hash__` coerente (mesmos atributos)
  quando o objeto for usado em `set` ou como chave de `dict`.
