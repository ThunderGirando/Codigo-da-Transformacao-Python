'''
Pedir para o usuário escrever o nome e idade
armazenar em variaveis
comparar a idade caso for 18 aparecer 'maior de idade' caso for menor aparecer ''menor de idade''
logo em se
'''

from datetime import date

# Obtém a data atual
hoje = date.today()

# Acessa o dia, mês e ano
ano_atual = hoje.year

nome = input('Qual seu nome? ')
idade = int(input("Qual sua idade? "))


print(f'Olá {nome}, Você tem {idade} anos de idade ')

# se (if) variavel idade_pessoa FOR (=> igual ou maior) que 18,
# a condição é ativada se nao (else) manda outra mensagem
if idade >= 18:
    print("Aparentemente você é maior de idade 😎 ta safe")
else:
    print("Aparentemente você é menor de idade 😅 ")


date.today
nascimento = (ano_atual - idade)
print(f'Você nasceu no ano de {nascimento} ') 

altura_pessoa = str(input("Qual sua altura? 'Exemplo: 1.70' "))

print(f'Você tem {altura_pessoa} de altura! ')
