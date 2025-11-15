'''


'''


def calcula_media(notas):
    """Calcula a média de uma lista de notas."""
    return sum(notas) / len(notas)

def verificar_aprovacao(media):
    """Verifica se o aluno foi aprovado (média >= 7)."""
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"
    
    
nome_aluno = input("Insira o nome do aluno: ")
notas_input = input("Insira as notas do aluno separadas por vírgula: ")
notas_aluno = [float(nota) for nota in notas_input.split(',')]

media_final = calcula_media(notas_aluno)
status_aluno = verificar_aprovacao(media_final)

print(f"Status do aluno: **{status_aluno}** com média: {media_final:.2f}")