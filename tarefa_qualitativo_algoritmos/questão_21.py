notas = []
opcao = ""

while opcao != "0":
    print("0 - Sair")
    print("1 - Inserir notas")
    print("2 - Retirar notas")
    print("3 - Mostrar notas")
    print("4 - Mostrar média")
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        nota = float(input("Digite a nota: "))
        notas.append(nota)
    elif opcao == "2":
        nota = float(input("Digite a nota: "))
        notas.remove(nota)
    elif opcao == "3":
        for nota in notas:
            print(nota)
    elif opcao == "4":
        soma = 0
        for nota in notas:
            soma += nota
        media = soma / len(notas)
        print(f"A média das notas é: {media}")
    elif opcao == "0":
        print("Saindo...")
    else:
        print("Opção inválida")