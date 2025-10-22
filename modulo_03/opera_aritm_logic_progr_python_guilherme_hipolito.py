# Funções de Operações
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    """Função que realiza a operação de Divisão."""
    # O Python vai gerar o erro se o b for 0
    return a / b

def menu_calculadora():
    executando = True

    while executando:
        # 1. Exibe o menu atualizado
        print("\n--- Menu Interativo ---")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação") # Opção 3
        print("4. Divisão")       # Opção 4
        print("5. Sair")          # Opção 5
        print("-----------------------")

        # 2. Recebe a opção
        escolha = input("Digite o número da opção desejada: ")

        # 3. Bloco de lógica (if/elif)
        if escolha == '1': # Soma
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = soma(num1, num2)
                print(f"\n✅ Resultado da Soma: {resultado}")
            except ValueError:
                print("\n❌ Entrada inválida. Por favor, digite números válidos.")

        elif escolha == '2': # Subtração
            try:
                num1 = float(input("Digite o primeiro número (Minuendo): "))
                num2 = float(input("Digite o segundo número (Subtraendo): "))
                resultado = subtracao(num1, num2)
                print(f"\n✅ Resultado da Subtração: {resultado}")
            except ValueError:
                print("\n❌ Entrada inválida. Por favor, digite números válidos.")

        elif escolha == '3': # Multiplicação
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = multiplicacao(num1, num2)
                print(f"\n✅ Resultado da Multiplicação: {resultado}")
            except ValueError:
                print("\n❌ Entrada inválida. Por favor, digite números válidos.")

        elif escolha == '4': # Divisão - O ponto que precisamos finalizar!
            try:
                num1 = float(input("Digite o dividendo: "))
                num2 = float(input("Digite o divisor: "))
                
                # A linha abaixo vai executar a divisão e gerar ZeroDivisionError se num2 for 0
                resultado = divisao(num1, num2)
                
                print(f"\n✅ Resultado da Divisão: {resultado}")

            # Precisamos adicionar o ZeroDivisionError aqui!
            # except...
                # print("\n...Mensagem de erro...")

            except ValueError:
                print("\n❌ Entrada inválida. Por favor, digite números válidos.")

        elif escolha == '5': # Sair (Condição final)
            executando = False
            print("\n👋 Programa encerrado. Obrigado por utilizar!")

        else:
            print("\n⚠️ Opção inválida. Por favor, escolha um número de 1 a 5.")


menu_calculadora()