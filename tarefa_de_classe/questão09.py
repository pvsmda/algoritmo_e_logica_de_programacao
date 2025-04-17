# Faça um algoritmo que imprima todos os números pares compreendidos entre 11 e 92. Depois
# some todos eles e imprima cada um deles e também a soma dos mesmos.
soma = []
for i in range(11, 93):
    if i % 2 == 0:
        print(i)
        soma.append(i)

print("A soma dos números pares entre 11 e 92 é:", sum(soma))
