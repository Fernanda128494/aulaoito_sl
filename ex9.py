nome1=input("Digite o primeiro nome ")
nome2=input("Digite o segundo nome ")
nome1=nome1.upper()
nome2=nome2.upper()
if (nome1 == "SENAC" or nome2=="CINELANDIA"):
    print(f"Bem vindo. {nome1} {nome2}")
else:
    print("Você não é SENAC")