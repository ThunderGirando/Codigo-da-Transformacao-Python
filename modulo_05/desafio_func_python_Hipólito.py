import json
import os


ARQUIVO_USUARIOS = 'modulo_05/usuarios.txt'


def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, 'r') as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                return {}
    return {}


def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, 'w') as arquivo:
        json.dump(usuarios, arquivo, indent=4)


def criar_conta(usuarios):
    usuario = input("Digite o nome de usuário: ").strip()
    if usuario in usuarios:
        print("Usuário já existe. Escolha outro nome.")
        return
    senha = input("Digite a senha: ").strip()
    usuarios[usuario] = senha
    print(f"Conta criada com sucesso para '{usuario}'!")


def fazer_login(usuarios):
    usuario = input("Digite o nome de usuário: ").strip()
    senha = input("Digite a senha: ").strip()
    if usuario in usuarios and usuarios[usuario] == senha:
        print(f"\nLogin bem-sucedido! Bem-vindo, {usuario}.")
    else:
        print("Usuário ou senha incorretos.")


def menu():
    usuarios = carregar_usuarios()
    while True:
        print("\n--- Sistema de Login ---")
        print("1. Criar Conta")
        print("2. Fazer Login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            criar_conta(usuarios)
        elif opcao == '2':
            fazer_login(usuarios)
        elif opcao == '3':
            salvar_usuarios(usuarios)
            print("Usuários salvos. Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
