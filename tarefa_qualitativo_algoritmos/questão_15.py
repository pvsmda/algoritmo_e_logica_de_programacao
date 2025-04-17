num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
opcao = input("Digite a opção desejada (+, -, *, /): ")

if opcao == "+":
    resultado = num1 + num2
    print(f"O resultado da adição foi: {resultado}")
elif opcao == "-":
    resultado = num1 - num2
    print(f"O resultado da subtração foi: {resultado}")
elif opcao == "*":
    resultado = num1 * num2
    print(f"O resultado da multiplicação foi: {resultado}")
elif opcao == "/":
    resultado = num1 / num2
    print(f"O resultado da divisão foi: {resultado}")