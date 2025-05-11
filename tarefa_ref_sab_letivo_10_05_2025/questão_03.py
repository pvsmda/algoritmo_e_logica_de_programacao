'''
Questão 03 -Faça um algoritmo que faça a união de dois vetores de mesmo tamanho e mesmo tipo em um ter
ceiro vetor com dobro do tamanho.
'''
# Criei o primeiro vetor com 5 elementos
vetor1 = [1, 2, 3, 4, 5]

# Criei o segundo vetor com 5 elementos também (mesmo tamanho e tipo do vetor1)
vetor2 = [6, 7, 8, 9, 10]

# Criei um terceiro vetor vazio que irá armazenar a união dos dois vetores
# A união neste caso será feita intercalando os elementos de vetor1 e vetor2
vetor3 = []

# Usei um laço for para percorrer os índices dos vetores
# Como os vetores têm o mesmo tamanho, usei range(len(vetor1)) para garantir que percorra todos os elementos
for i in range(len(vetor1)):
    # Adicionei ao vetor3 o elemento da posição i do vetor1
    vetor3.append(vetor1[i])
    
    # Em seguida, adicionei o elemento da posição i do vetor2
    vetor3.append(vetor2[i])

# Ao final do laço, vetor3 conterá todos os elementos de vetor1 e vetor2 intercalados
print(vetor3)
