import shutil
import os


PASTA_ORIGEM = 'modulo_06/arquivos_importantes'  
PASTA_BACKUP = 'modulo_06/backup'  


os.makedirs(PASTA_ORIGEM, exist_ok=True)
os.makedirs(PASTA_BACKUP, exist_ok=True)


with open(os.path.join(PASTA_ORIGEM, 'dados.txt'), 'w', encoding='utf-8') as f:
    f.write("Dados importantes\n")
with open(os.path.join(PASTA_ORIGEM, 'config.py'), 'w', encoding='utf-8') as f:
    f.write("# Configurações\n")


def backup_automatico():
    try:
        for arquivo in os.listdir(PASTA_ORIGEM):
            caminho_origem = os.path.join(PASTA_ORIGEM, arquivo)
            caminho_destino = os.path.join(PASTA_BACKUP, arquivo)
            if os.path.isfile(caminho_origem):
                shutil.copy(caminho_origem, caminho_destino)
                print(f"Arquivo {arquivo} copiado para backup.")
        print("Backup automático concluído com sucesso!")
    except Exception as e:
        print(f"Erro durante o backup: {e}")


backup_automatico()
