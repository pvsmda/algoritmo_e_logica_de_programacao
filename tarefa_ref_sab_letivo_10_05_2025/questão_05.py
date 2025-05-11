'''
Questão 05 - Crie três vetores, de modo que o usuário preencha a quantidade de elementos do primeiro vetor
e depois do segundo vetor com valores em reais em cada um deles. O terceiro vetor vai receber e imprimir na tela a soma de seus elementos em cada posição correspondente de ambos os vetores.
'''

# Iniciei as três listas vazias
vetor1 = []
vetor2 = []
vetor3 = []

# Solicitei ao usuário a quantidade de elementos para o primeiro vetor
n1 = int(input("Digite a quantidade de elementos do primeiro vetor: "))

# Preenchi o primeiro vetor com valores reais informados pelo usuário
for i in range(n1):
    valor = float(input(f"Digite o {i+1}º valor do primeiro vetor (R$): "))
    vetor1.append(valor)

# Solicitei ao usuário a quantidade de elementos para o segundo vetor
n2 = int(input("Digite a quantidade de elementos do segundo vetor: "))

# Preenchi o segundo vetor com valores reais informados pelo usuário
for i in range(n2):
    valor = float(input(f"Digite o {i+1}º valor do segundo vetor (R$): "))
    vetor2.append(valor)

# Defini o tamanho mínimo entre os dois vetores para evitar erro de índice
tamanho_minimo = min(len(vetor1), len(vetor2))

# Criei o terceiro vetor somando os valores correspondentes nas mesmas posições
for i in range(tamanho_minimo):
    soma = vetor1[i] + vetor2[i]
    vetor3.append(soma)

# Imprimi o terceiro vetor com os resultados das somas
print("Vetor resultante (soma dos elementos nas mesmas posições):")
print(vetor3)

