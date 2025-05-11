'''
Questão 08 - Crie um vetor que armazene o nome de qualquer quantidade de alunos. Um segundo vetor que
armazene qualquer quantidade de notas para cada estudante e um terceiro vetor que armazene as
médias de cada estudante. No final imprima em cada linha o nome do estudante com todas as notas a
frente, e no final a média.
'''
# Criamos três listas (vetores) vazias:
# 'nome_alunos' para armazenar os nomes dos alunos
# 'nota_alunos' para armazenar as notas de cada aluno
# 'media_alunos' para armazenar as médias dos alunos
nome_alunos = []
nota_alunos = []
media_alunos = []

# Solicita ao usuário a quantidade de alunos
n = int(input("Digite a quantidade de alunos: "))

# Usamos um laço para repetir o processo de entrada de dados 'n' vezes
for i in range(n):
    # Lê o nome do aluno e adiciona ao vetor de nomes
    nome_alunos.append(input(f"Digite o {i+1}º nome: "))
    
    # Lê as notas do aluno e adiciona ao vetor de notas
    notas = []  # Lista temporária para armazenar as notas de cada aluno
    for j in range(3):  # Considera que são 3 notas por aluno
        # Solicita a nota e a adiciona na lista 'notas'
        notas.append(float(input(f"Digite a {j+1}º nota do {i+1}º aluno: ")))
    
    # Adiciona a lista de notas do aluno na lista 'nota_alunos'
    nota_alunos.append(notas)

    # Calcula a média das notas do aluno e adiciona ao vetor de médias
    media_alunos.append(sum(notas) / len(notas))  # 'sum' soma as notas e 'len' conta o número de notas

# Após coletar os dados, vamos imprimir as informações de cada aluno
for i in range(n):
    # Imprime o nome do aluno
    print(f"Nome: {nome_alunos[i]}")
    
    # Imprime as notas do aluno
    print(f"Notas: {nota_alunos[i]}")
    
    # Imprime a média do aluno
    print(f"Média: {media_alunos[i]}")
    
    # Imprime uma linha em branco para separar os alunos
    print()
