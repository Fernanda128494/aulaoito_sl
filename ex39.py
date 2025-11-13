def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multi(a, b):
    return a * b  
def div(a, b):
    if a != 0:
     return a/b
    else:
        print("Valor inválido")
escolha=""
while escolha != "0":     
    escolha=input("Digite uma opção 1-somar, 2-subtrair, 3-mltiplicar, 4-dividir, 0-parar")
    num1= int(input("Digite o primeiro número "))
    num2= int(input("Digite o primeiro número "))
    if escolha == "1":
        x=soma(num1, num2)
    elif escolha == "2":
        x=subtrair(num1, num2)  
    elif escolha == "3":
        x=multi(num1, num2)
    elif escolha == "4":
        x=div(num1, num2)
    else:
        break        
    print(f"Resultado da operação: {x}")