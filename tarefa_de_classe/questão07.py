# Faça um algoritmo em que calcula o delta e as raízes reais da seguinte equação do segundo grau:
# x2-3x+2 =0

a = int(input("Digite o valor de a:"))
b = int(input("Digite o valor de b:"))
c = int(input("Digite o valor de c:"))

delta = (b ** 2) - (4 * a * c)

if delta > 0:
    x1 = (-b + delta ** (1/2)) / (2 * a)
    x2 = (-b - delta ** (1/2)) / (2 * a)
    print("O valor de x1 é:", x1)
    print("O valor de x2 é:", x2)
else:
    print("Delta negativo, impossivel calcular raizes reais")
