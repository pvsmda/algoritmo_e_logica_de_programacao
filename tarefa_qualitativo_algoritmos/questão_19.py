produtos_vendidos = int(input("Digite a quantidade de produtos vendidos: "))
salario_bruto = 5500.00
salario_final = salario_bruto - (salario_bruto * 0.09) - (salario_bruto * 0.11) + (salario_bruto * 0.02 * produtos_vendidos)

print(f"O salário final do funcionário foi: {salario_final}")