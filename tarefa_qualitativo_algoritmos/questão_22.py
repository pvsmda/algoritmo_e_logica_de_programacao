print("===============Cardápio TIMONBURGUER==============")
print("Cachorro quente     |100   |4.20")
print("Bauru simples       |101   |8.50")
print("X- burguer          |102   |9.50")
print("Hamburguer          |103   |8.00")
print("Cheeseburguer       |104   |10.30")
print("Refrigerante Ks     |105   |4.00")
print("Refrigerante 1L     |106   |10.00")
print("Suco de Fruta (copo)|107   |6.50")
print("\n==================================================\n")

total = 0

while True:
    codigo = int(input("Digite o codigo do produto (ou 0 para sair): "))
    if codigo == 0:
        break
    quantidade = int(input("Digite a quantidade: "))
    if codigo == 100:
        total += quantidade * 4.20
    elif codigo == 101:
        total += quantidade * 8.50
    elif codigo == 102:
        total += quantidade * 9.50
    elif codigo == 103:
        total += quantidade * 8.00
    elif codigo == 104:
        total += quantidade * 10.30
    elif codigo == 105:
        total += quantidade * 4.00
    elif codigo == 106:
        total += quantidade * 10.00
    elif codigo == 107:
        total += quantidade * 6.50
    else:
        print("Código inválido!")

print(f"Total: R$ {total:.2f}")

pagamento = float(input("Digite o valor do pagamento: "))
troco = pagamento - total

print("===============CUPOM FISCAL=======================")
print(f"Total: R$ {total:.2f}")
print(f"Troco: R$ {troco:.2f}")
