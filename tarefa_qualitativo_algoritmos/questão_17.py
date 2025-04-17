print("--------Caixa Rápido Bancário--------")
conta = input("Digite o número da conta: ")

saldo = 0.0
extrato = []
opcao = ""

while opcao != "5":
    print("--------Menu--------")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Saldo")
    print("4 - Extrato")
    print("5 - Sair")
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        saldo += valor
        extrato.append(f"Depósito: {valor}")
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        if valor > saldo:
            print("Saldo insuficiente")
        else:
            saldo -= valor
            extrato.append(f"Saque: {valor}")
    elif opcao == "3":
        print(f"Seu saldo atual é: {saldo}")
    elif opcao == "4":
        for movimento in extrato:
            print(movimento)
    elif opcao == "5":
        print("Saindo...")
    else:
        print("Opção inválida")

print("--------Caixa Rápido Bancário--------")