def eh_par(numero):
    return numero % 2==0
num=int(input("Digite um número inteiro "))
resultado=eh_par(num) 
if resultado:
    print(f'O número {num} é par')  
else:
    print(f"O número {num} é ímpar")         