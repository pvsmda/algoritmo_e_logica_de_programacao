'''
Questão 07 - Crie três vetores, sendo que no primeiro é registrado o nome de cada funcionário da empresa.
No segundo é registrado os cpf de cada um deles e, no terceiro junte o nome ao cpf e imprima na tela
o nome, seguido do cpf em cada uma das linhas.
'''

# Criei três listas (vetores) vazias:
# 'nomes' para armazenar os nomes dos funcionários
# 'cpfs' para armazenar os CPFs dos funcionários
# 'funcionarios' para armazenar a junção de nome e CPF
nomes = []
cpfs = []
funcionarios = []

# Solicita ao usuário a quantidade de funcionários que serão cadastrados
n = int(input("Digite a quantidade de funcionários: "))

# Utilizamos um laço para preencher as listas com os dados dos funcionários
for i in range(n):
    # Lê o nome do funcionário e adiciona na lista 'nomes'
    nome = input(f"Digite o nome do {i+1}º funcionário: ")
    # Lê o CPF do funcionário e adiciona na lista 'cpfs'
    cpf = input(f"Digite o CPF do {i+1}º funcionário: ")
    
    # Adiciona o nome à lista 'nomes'
    nomes.append(nome)
    # Adiciona o CPF à lista 'cpfs'
    cpfs.append(cpf)

# Agora criei o vetor 'funcionarios', que armazenará o nome e CPF de cada funcionário.
for i in range(n):
    # Junta o nome e o CPF do funcionário na forma "nome - CPF" e adiciona no vetor 'funcionarios'
    funcionarios.append(f"{nomes[i]} - {cpfs[i]}")

# Exibe a lista de funcionários com nome e CPF em cada linha
print("\nLista de Funcionários:")
# utilizei um laço para imprimir cada item da lista 'funcionarios'
for dados in funcionarios:
    # Imprime cada linha com o nome e CPF do funcionário
    print(dados)
