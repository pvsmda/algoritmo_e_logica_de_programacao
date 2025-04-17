# Escreva um código em que o usuário digite três números e o programa diga qual o maior.
num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
num3 = int(input("Digite o terceiro número:"))

if num1 > num2 and num1 > num3:
    print(f"O {num1} é o maior")
elif num2 > num1 and num2 > num3:
    print(f"O {num2} é o maior")
else:
    print(f"O {num3} é o maior")
