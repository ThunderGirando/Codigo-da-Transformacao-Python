import csv
import os


ARQUIVO_CSV = 'modulo_06/notas.csv'


def carregar_notas():
    notas = []
    if os.path.exists(ARQUIVO_CSV):
        with open(ARQUIVO_CSV, 'r', newline='', encoding='utf-8') as arquivo:
            reader = csv.DictReader(arquivo)
            for row in reader:
                notas.append(row)
    return notas


def salvar_notas(notas):
    if notas:
        with open(ARQUIVO_CSV, 'w', newline='', encoding='utf-8') as arquivo:
            fieldnames = ['nome', 'disciplina', 'nota']
            writer = csv.DictWriter(arquivo, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(notas)


notas = carregar_notas()


nome = input("Digite o nome do aluno: ")


while True:
    disciplina = input("Digite a disciplina (ou 'fim' para parar): ")
    if disciplina.lower() == 'fim':
        break
    try:
        nota = float(input("Digite a nota: "))
    except ValueError:
        print("Nota inválida. Digite um número.")
        continue

   
    nova_nota = {
        'nome': nome,
        'disciplina': disciplina,
        'nota': nota
    }

   
    notas.append(nova_nota)


salvar_notas(notas)



notas_por_aluno = {}
for nota in notas:
    nome = nota['nome']
    disciplina = nota['disciplina']
    nota_valor = nota['nota']
    if nome not in notas_por_aluno:
        notas_por_aluno[nome] = {}
    notas_por_aluno[nome][disciplina] = nota_valor


print("\nNotas armazenadas:")
for nome, disciplinas in notas_por_aluno.items():
    print(f"{nome}: ", end="")
    for disciplina, nota in disciplinas.items():
        print(f"{disciplina}: {nota} / ", end="")
    print()
