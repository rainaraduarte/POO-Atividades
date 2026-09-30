"""Lista 2 - Questão 10 (Nível 3): caixa_eletronico.py

Menu em laço (depositar, sacar, saldo, sair). Nenhuma entrada do usuário
pode derrubar o programa; o menu captura ErroDeConta para os erros do domínio.

Rode a partir desta pasta:  python caixa_eletronico.py
"""

from conta_bancaria import ContaBancaria, ErroDeConta

MENU = """
=== Caixa Eletrônico ===
1 - Depositar
2 - Sacar
3 - Ver saldo
4 - Sair
"""


def ler_valor(mensagem: str) -> float:
    """Lê um número. Aceita vírgula decimal. Lança ValueError se inválido."""
    texto = input(mensagem).strip().replace(",", ".")
    return float(texto)  # ValueError se não for número


def main() -> None:
    conta = ContaBancaria("Cliente")

    while True:
        print(MENU)
        try:
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                conta.depositar(ler_valor("Valor do depósito: R$ "))
                print("Depósito realizado.")
            elif opcao == "2":
                conta.sacar(ler_valor("Valor do saque: R$ "))
                print("Saque realizado.")
            elif opcao == "3":
                print(f"Saldo atual: R$ {conta.saldo:.2f}")
            elif opcao == "4":
                print("Obrigado por usar o caixa. Até logo!")
                break
            else:
                print("Opção inválida. Escolha de 1 a 4.")

        except ErroDeConta as erro:      # erros do domínio (3 tipos)
            print(f"Operação negada: {erro}")
        except ValueError:               # entrada que não é número
            print("Entrada inválida: digite apenas números (ex.: 150,50).")
        except (EOFError, KeyboardInterrupt):  # Ctrl+D / Ctrl+C
            print("\nEncerrando o caixa.")
            break


if __name__ == "__main__":
    main()
