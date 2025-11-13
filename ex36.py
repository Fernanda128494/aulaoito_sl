numero_secreto=42
palpite=0
print("Tente adivinhar o número secreto entre 1 e 100.")
while palpite != numero_secreto:
    try:
        entrada=input("Seu palpite: ")
        palpite=int(entrada)
        if palpite < numero_secreto:
         print("Muito baixo, tente um número maior.")
        elif palpite > numero_secreto:
         print("Muito alto, tente um número menor.")
        else:
            print("Parabéns! Você acertou o númer secreto!")
    except ValueError:
        print("Por favor, digite apenas números inteiros.")         