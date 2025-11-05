cargo=input("Digite seu cargo ")
if cargo=="caixa":
    salario=1500
elif cargo=="vendedor":
    salario=2400
elif cargo=="gerente":
    salario=4000
else:
    salario=0
    print("Cargo inválido")
inss= salario*0.12
if salario >2000:
    irrf=salario*0.14
else:
    irrf=salario*0.08        
final=salario-inss-irrf                
print(f"Seu salário líquido é {final}")
