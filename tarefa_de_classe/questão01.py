# Faça um algoritmo que ler três números inteiros qualquer nas variáveis a, b e c e os imprima em
# ordem crescente, utilizando-se somente de comandos simples e o código mais enxuto possível.

a = int(input("Digite o primeiro número:"))
b = int(input("Digite o segundo número:"))
c = int(input("Digite o terceiro número:"))

if a > b:
    a,b = b,a
if a > c:
    a,c = c,a
if b > c:
    b,c = c,b

print("Ordem crescente:", a,b,c)

