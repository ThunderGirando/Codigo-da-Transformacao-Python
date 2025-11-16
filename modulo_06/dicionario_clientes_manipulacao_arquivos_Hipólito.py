import json
import os


ARQUIVO_CLIENTES = 'modulo_06/clientes.json'


def carregar_clientes():
    if os.path.exists(ARQUIVO_CLIENTES):
        with open(ARQUIVO_CLIENTES, 'r', encoding='utf-8') as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                return []
    return []


def salvar_clientes(clientes):
    with open(ARQUIVO_CLIENTES, 'w', encoding='utf-8') as arquivo:
        json.dump(clientes, arquivo, indent=4, ensure_ascii=False)


clientes = carregar_clientes()


nome = input("Digite o nome do cliente: ")
idade = int(input("Digite a idade do cliente: "))
cidade = input("Digite a cidade do cliente: ")


novo_cliente = {
    'nome': nome,
    'idade': idade,
    'cidade': cidade
}


clientes.append(novo_cliente)


salvar_clientes(clientes)


print("\nInformações de todos os Clientes armazenados:")
for i, cliente in enumerate(clientes, start=1):
    print(f"\nCliente {i}:")
    print(f"Nome: {cliente['nome']}")
    print(f"Idade: {cliente['idade']}")
    print(f"Cidade: {cliente['cidade']}")
