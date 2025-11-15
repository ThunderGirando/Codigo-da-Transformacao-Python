import random


def maior_menor(numeros):
    if not numeros:
        return None, None
    maior = max(numeros)
    menor = min(numeros)
    return maior, menor


numeros = []
for _ in range(10):
    num = round(random.uniform(1, 10), 1)
    numeros.append(num)

print("Lista de números gerados:")
for num in numeros:
    print(num)


maior, menor = maior_menor(numeros)
print(f"\nMaior valor: {maior}")
print(f"Menor valor: {menor}")
