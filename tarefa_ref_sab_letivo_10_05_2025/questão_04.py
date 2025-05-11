'''
Questão 04 - Faca um algoritmo que possua um vetor com 10 elementos. Depois faça a troca do último ele-
mento com o primeiro.
'''
# Criei um vetor chamado vetor1 com 10 elementos, de 1 a 10
vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Armazena temporariamente o primeiro elemento do vetor (posição 0) na variável auxiliar 'aux'
aux = vetor1[0]

# Substitui o primeiro elemento do vetor (posição 0) pelo último elemento (posição -1)
# Em Python, o índice -1 sempre representa o último elemento da lista
vetor1[0] = vetor1[-1]

# Agora coloca-se o valor que estava no início (armazenado em 'aux') na última posição do vetor
vetor1[-1] = aux

# Por fim, imprime o vetor1 após a troca dos elementos
print(vetor1)
