'''
Questão 06 - Crie três vetores, sendo que no primeiro é registrado respectivamente o nome e cpf de cada cli-
ente. No segundo registre e imprima somente os nomes de cada um deles e, no terceiro somente a re-
lação de todos os cpf.
'''
# Criamos três vetores (listas vazias)
vetor_nome = []       # Vai armazenar os nomes dos clientes
vetor_cpf = []        # Vai armazenar os CPFs dos clientes
vetor_relacao = []    # Vai armazenar a junção de nome e CPF (relacionamento entre eles)

# Solicitamos ao usuário a quantidade de clientes que serão cadastrados
n = int(input("Digite a quantidade de clientes: "))

# Usamos um laço para repetir o processo de entrada de dados 'n' vezes
for i in range(n):
    # Lê o nome do cliente e adiciona ao vetor de nomes
    vetor_nome.append(input(f"Digite o {i+1}º nome: "))
    
    # Lê o CPF do cliente e adiciona ao vetor de CPFs
    vetor_cpf.append(input(f"Digite o {i+1}º CPF: "))

# Outro laço para criar a relação entre nome e CPF
for i in range(n):
    # Cria uma string com o nome e o CPF separados por hífen e adiciona ao vetor de relação
    vetor_relacao.append(vetor_nome[i] + " - " + vetor_cpf[i])

# Imprime a relação final com os dados de cada cliente
print(vetor_relacao)
