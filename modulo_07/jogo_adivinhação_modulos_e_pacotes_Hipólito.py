import random
import math


numero_secreto = random.randint(1, 100)
tentativas = 0

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 100.")

while True:
    try:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1
        if palpite < numero_secreto:
            print("Muito baixo!")
        elif palpite > numero_secreto:
            print("Muito alto!")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            raiz = math.sqrt(numero_secreto)
            print(f"O número secreto era {numero_secreto}, e sua raiz quadrada é {raiz:.2f}")
            break
    except ValueError:
        print("Digite um número válido.")
