nome=""
while nome != "SAIR":
    nome=input("Digite seu nome ").upper()
    if nome == "SAIR":
       break
    else:       
       print(F"Olá, {nome}!")