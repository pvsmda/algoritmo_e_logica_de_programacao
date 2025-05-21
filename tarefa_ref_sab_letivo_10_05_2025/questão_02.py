'''
Questão 02 - Faça um algoritmo que some o conteúdo de dois vetores e armazene o resultado em um terceiro
vetor.
'''
vetor1 = [1, 2, 3, 4, 5]
vetor2 = [6, 7, 8, 9, 10]
vetor3 = []

for i in range(len(vetor1)):
    vetor3.append(vetor1[i] + vetor2[i])

print(vetor3)
