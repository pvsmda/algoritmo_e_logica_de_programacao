camisas = int(input("Digite a quantidade de camisas: "))
camisaP = int(input("Digite a quantidade de camisas de tamanho P: "))
camisaPP = int(input("Digite a quantidade de camisas de tamanho PP: "))
camisaM = int(input("Digite a quantidade de camisas de tamanho M: "))
camisaG = int(input("Digite a quantidade de camisas de tamanho G: "))

soma_camisas = camisaP + camisaPP + camisaM + camisaG

if soma_camisas > camisas:
    print("A quantidade ultrapassa a quantidade desejada")
else:
    total = (camisaP * 15) + (camisaPP * 15) + (camisaM * 18) + (camisaG * 20)

    print(f"O valor total da compra foi: {total}")
    print(f"A quantidade de camisas de tamanho P foi: {camisaP}")
    print(f"A quantidade de camisas de tamanho PP foi: {camisaPP}")
    print(f"A quantidade de camisas de tamanho M foi: {camisaM}")
    print(f"A quantidade de camisas de tamanho G foi: {camisaG}")
