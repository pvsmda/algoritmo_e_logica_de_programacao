'''
Questão 01)

texto = input("Digite um texto: ")
contador = 0

for caractere in texto:
    if caractere != " ":
        contador += 1
print(f"O texto tem {contador} letras")
'''

'''
Questão 02)

numero = int(input("Digite um numero: "))
fatorial = 1

for i in range (1, numero + 1):
    fatorial *= i

print(f"A fatorial de {numero} é: {fatorial}")
'''

'''
Questão 03)
numeroDeTextos = int(input("Digite o numero de textos que voce quer digitar: "))
texto = ""

for i in range(numeroDeTextos):
    entrada = input(f"Digite o texto {i + 1}: ")
    texto += entrada + " "
print("Texto concatenado: ")
print(texto.strip())
'''


'''
Questão 04)

texto = input("Digite um texto: ")
vogais = 'aeiouAEIOUáéíóú'
contador = 0
posicoes = []

for i, char in enumerate(texto):
    if char in vogais:
        contador += 1
        posicoes.append(i)

print(f"O texto possui: {contador} vogais")
print(f"Posições das vogais: {posicoes}")
'''

'''
Questão 05)
nome = input("Digite um nome: ").lower()
letra = input("Digite uma letra: ").lower()
contador = 0

for caractere in nome:
    if caractere == letra:
        contador += 1
if contador > 0:
    print(f"A letra: {letra} pertence ao nome {nome} e aparece {contador} vezes")
else:
    print(f"A letra: {letra} não pertence ao nome: {nome}")
'''

'''
Questão 06)

numero = float(input("Digite um número para ver sua tabuada de divisão: "))

for i in range(1, 11):
    resultado =  numero / i
    print(f"{numero} ÷ {i} = {resultado}")
'''

'''
Questão 07) 

soma = 0

for i in range(1, 6):
    numero = float(input(f"Digite o {i}º número: "))
    soma += numero

media = soma / 5

print(f"A média aritmética dos números é: {media:.2f}")

'''

'''
Questão 08)

for numero in range(3, 31):
    primo = True 
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")

'''





