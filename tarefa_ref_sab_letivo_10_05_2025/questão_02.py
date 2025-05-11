'''
Questão 02 - Faça um algoritmo que some o conteúdo de dois vetores e armazene o resultado em um terceiro
vetor.
'''
# Criei o primeiro vetor com os valores de 1 a 5
vetor1 = [1, 2, 3, 4, 5]

# Criei o segundo vetor com os valores de 6 a 10
vetor2 = [6, 7, 8, 9, 10]

# Criei um terceiro vetor vazio que irá armazenar a soma dos elementos de vetor1 e vetor2
vetor3 = []

# Usei um laço for para percorrer os índices dos vetores
# A função len(vetor1) retorna o tamanho do vetor1, que é 5
for i in range(len(vetor1)):
    # Para cada índice i, soma-se os elementos correspondentes de vetor1 e vetor2
    # Exemplo: vetor1[0] + vetor2[0] = 1 + 6 = 7
    # O resultado é adicionado (append) ao final do vetor3
    vetor3.append(vetor1[i] + vetor2[i])

# Após o laço, imprime o vetor3, que contém as somas dos elementos de vetor1 e vetor2
print(vetor3)
