soma_positivo=0
numero=-1
while numero != 0:
    entrada=input("Digite um número (0 para parar): ")
    try:
        numero=int(entrada)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro")
        continue
    if numero > 0:
        soma_positivo=soma_positivo + numero    
print(f"A soma dos números positivos é {soma_positivo}")        