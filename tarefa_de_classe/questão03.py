#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
#Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45
#para viagens mais longas.

distancia = float(input("DIgite a distancia que deseja percorrer:"))

if distancia <= 200:
    preco = distancia * 0.50
    print("O preço {} da passagem é:".format(preco, distancia))
else:
    preco = distancia * 0.45
    print("O preço {} da passagem é:".format(preco, distancia))

