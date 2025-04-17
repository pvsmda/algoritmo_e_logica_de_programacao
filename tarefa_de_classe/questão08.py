#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O
#programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor
#da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como
#sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valorDaCasa = float(input("Digite o valor da casa:"))
salarioDoComprador = float(input("Digite quanto é salário:"))
anos = int(input("Digite em quantos anos deseja pagar:"))

meses = anos * 12
prestacaoDaCasa = valorDaCasa / meses

if prestacaoDaCasa > salarioDoComprador * 0.30:
    print("empréstimo negado")
else:
    print("emprestimo aprovado")
