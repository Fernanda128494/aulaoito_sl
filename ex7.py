n1=float(input("digite a primeira nota "))
n2=float(input("digite a segunda nota "))
n3=float(input("digite a terceira nota "))
n4=float(input("digite a quarta nota "))
media=(n1+n2+n3+n4)/4
if (media>=6):
    print(f"Você está Aprovado, sua média é {media}")
else:
    print(f"Você está em Recuperação, sua média é {media}")   