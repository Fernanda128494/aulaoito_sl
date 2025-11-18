import pandas as pd 
cargos = []
salarios = []
qtd = int(input("Quantos cargos deseja cadastrar? "))
for i in range(qtd):
    print(f"Cadastro {i + 1}: ")
    cargo =input("Digite o cargo: ")
    salario = float(input("Digite o saláro: "))
    cargos.append(cargo)
    salarios.append(salario)
dados = {'cargos': cargos, 'salarios': salarios}
dados_bi = pd.DataFrame(dados)
print("Tabela de cargos e Salários:")
print(dados_bi)    