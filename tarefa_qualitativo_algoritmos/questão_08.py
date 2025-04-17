nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("A sua média é:", media)
    print("Nota suficiente")
else:
    print("A sua média é: ", media)
    print("Nota insuficiente")