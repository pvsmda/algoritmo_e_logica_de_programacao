temperatura = float(input("Digite a temperatura: "))
opcao = input("Escolha C para Celsius ou F para Fahrenheit: ").upper()
if opcao == "C":    # Celsius para Fahrenheit
    fahrenheit = (temperatura * 9/5) + 32
    print(f"A temperatura em Fahrenheit é {fahrenheit}")
else:               # Fahrenheit para Celsius
    celsius = (temperatura - 32) * 5/9
    print(f"A temperatura em Celsius é {celsius}")