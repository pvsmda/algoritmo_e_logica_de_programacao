'''
Questão 01 - Faça um algoritmo que copie o conteúdo de um vetor em um segundo vetor.
'''

# Criei uma lista chamada 'vetor' com os elementos de 1 a 5
vetor = [1, 2, 3, 4, 5]

# Usei o método .copy() para fazer uma cópia da lista 'vetor'
# A nova lista é armazenada na variável 'vetor_copia'
# Observação: 'vetor' e 'vetor_copia' são listas independentes na memória
vetor_copia = vetor.copy()

# Imprimindo o conteúdo da lista original
print(vetor)

# Imprimindo o conteúdo da cópia da lista
print(vetor_copia)
