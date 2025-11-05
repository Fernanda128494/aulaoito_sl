produto=input("Digite o produto ")
qtd=int(input("Digite a quantidade "))
if produto=="mouse":
    valor=10
elif produto=="teclado":
    valor=20
elif produto=="memoria":
    valor=100
else:
    valor=0
    print("Produto inválido")
total= valor*qtd
if qtd >=10:
    imposto=total*0.05
else:
    imposto=total*0.10       
final=total+imposto 
print(f"Valor total dos produtos é {total}") 
print(f"Valor do imposto é {imposto}")             
print(f"O valor total a pagar é {final}")
