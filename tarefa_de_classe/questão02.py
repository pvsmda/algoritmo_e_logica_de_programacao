# Elabore um programa em que o usuário digita um ano qualquer e o algoritmo diz se aquele ano é ou não bissexto.
ano = int(input("Digite um ano:"))
if ano % 4 == 0 :
    print("O ano {} é bissexto".format(ano))
else:
    print("O ano {} não é bissexto".format(ano))

