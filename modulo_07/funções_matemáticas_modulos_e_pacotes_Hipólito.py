import utilidades

def menu():
    print("\nEscolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz Quadrada")
    print("7. Fatorial")
    print("8. Sair")

while True:
    menu()
    try:
        escolha = int(input("Digite o número da operação: "))
        if escolha == 8:
            print("Saindo...")
            break
        elif escolha == 1:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print(f"Resultado: {a} + {b} = {utilidades.soma(a, b)}")
        elif escolha == 2:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print(f"Resultado: {a} - {b} = {utilidades.subtracao(a, b)}")
        elif escolha == 3:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print(f"Resultado: {a} * {b} = {utilidades.multiplicacao(a, b)}")
        elif escolha == 4:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print(f"Resultado: {a} / {b} = {utilidades.divisao(a, b)}")
        elif escolha == 5:
            a = float(input("Digite a base: "))
            b = float(input("Digite o expoente: "))
            print(f"Resultado: {a} ** {b} = {utilidades.potencia(a, b)}")
        elif escolha == 6:
            a = float(input("Digite o número: "))
            print(f"Resultado: sqrt({a}) = {utilidades.raiz_quadrada(a)}")
        elif escolha == 7:
            a = int(input("Digite o número: "))
            print(f"Resultado: {a}! = {utilidades.fatorial(a)}")
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número.")
