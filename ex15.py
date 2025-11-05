nasc = int(input("Digite o ano de nascimento: "))
genero = input("Digite o gênero (m ou f) ").upper()
idade= 2025 - nasc
if idade >= 18 and genero=="M":
    print(f"Você tem {idade} anos e está apto a se alistar")
else:
    print("Você não está apto")