#Faça uma calculadora com as operações de soma, subtração, multiplicação, divisão, radiciação
#e potenciação.

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
op = input("Digite a operação desejada:")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "**":
    print(num1 ** num2)
elif op == "r":
    print(num1 ** (1/num2))


