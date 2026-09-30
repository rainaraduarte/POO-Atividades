"""E13 - Revisão: try / except / else / finally."""


def dividir(entrada: str) -> None:
    try:
        valor = float(entrada)
        resultado = 100 / valor
    except ValueError:
        print("Digite um número.")
    except ZeroDivisionError:
        print("Não dá para dividir por zero.")
    else:
        # roda só se NÃO houve exceção
        print(f"Resultado: {resultado}")
    finally:
        # roda SEMPRE (limpeza)
        print("Fim da operação.")


if __name__ == "__main__":
    for texto in ("4", "abc", "0"):
        print(f"--- entrada: {texto!r}")
        dividir(texto)

    # Toda exceção é um objeto de uma classe que herda de Exception.
    # except ValueError também captura SUBCLASSES de ValueError.
    print(ValueError.__mro__)
    print(issubclass(ZeroDivisionError, ArithmeticError))  # True
