quantidade_notas = int(input("Digite a quantidade de notas: "))
soma = 0

for i in range(quantidade_notas):
    nota = float(input("Digite a nota: "))
    soma += nota

media = soma / quantidade_notas

if media >= 7:
    print("A sua média é:", media)
    print("Nota suficiente")
else:
    print("A sua média é: ", media)
    print("Nota insuficiente")