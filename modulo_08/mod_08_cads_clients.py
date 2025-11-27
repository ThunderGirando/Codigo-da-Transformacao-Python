import json

ARQUIVO_DADOS = "modulo_08/clientes_data.json"

class Cliente:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def to_dict(self):
        return {"nome": self.nome, "idade": self.idade, "cidade": self.cidade}

class SistemaCadastro:
    def __init__(self, arquivo_dados):
        self.arquivo_dados = arquivo_dados
        self.clientes = self._carregar_dados()

    def _carregar_dados(self):
        try:
            # Abrindo o arquivo com encoding 'utf-8' para leitura correta
            with open(self.arquivo_dados, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                return [Cliente(**d) for d in dados]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def salvar_dados(self):
        dados_para_salvar = [cliente.to_dict() for cliente in self.clientes]
        # Chave para acentos: ensure_ascii=False e encoding='utf-8'
        with open(self.arquivo_dados, 'w', encoding='utf-8') as f:
            json.dump(dados_para_salvar, f, indent=4, ensure_ascii=False)

    def adicionar_cliente(self, nome, idade, cidade):
        novo_cliente = Cliente(nome, idade, cidade)
        self.clientes.append(novo_cliente)
        self.salvar_dados()
        print(f"Cliente '{nome}' adicionado e dados salvos.")

    def remover_cliente(self, indice):
        try:
            cliente_removido = self.clientes.pop(indice - 1) 
            self.salvar_dados()
            print(f"Cliente '{cliente_removido.nome}' removido com sucesso e dados salvos.")
            return True
        except IndexError:
            print("ERRO: Índice de cliente inválido.")
            return False

    def listar_clientes(self):
        if not self.clientes:
            print("\nNenhum cliente cadastrado.")
            return False

        print("\n--- Lista de Clientes ---")
        for i, cliente in enumerate(self.clientes, 1):
            print(f"{i}. Nome: {cliente.nome}, Idade: {cliente.idade}, Cidade: {cliente.cidade}")
        print("-------------------------")
        return True


def _obter_dados_cliente():
    print("\n--- Entrada de Dados ---")
    
    nome = input("Digite o Nome do Cliente: ").strip()
    if not nome:
        print("Nome não pode ser vazio. Operação cancelada.")
        return None, None, None

    while True:
        try:
            idade = int(input("Digite a Idade do Cliente: "))
            if 0 < idade <= 150:
                break
            print("Idade inválida.")
        except ValueError:
            print("Entrada inválida. Digite a idade usando apenas números inteiros.")

    cidade = input("Digite a Cidade do Cliente: ").strip()
    
    return nome, idade, cidade


def _remover_cliente(sistema):
    if not sistema.listar_clientes():
        return

    while True:
        try:
            indice = int(input("Digite o NÚMERO do cliente para remover (ou 0 para cancelar): "))
            if indice == 0:
                print("Operação de remoção cancelada.")
                return
            if 1 <= indice <= len(sistema.clientes):
                sistema.remover_cliente(indice)
                break
            else:
                print("Número inválido. Por favor, digite um número da lista.")
        except ValueError:
            print("Entrada inválida. Digite apenas o número do cliente.")


def menu_principal():
    sistema = SistemaCadastro(ARQUIVO_DADOS)

    while True:
        print("\n=== Menu do Sistema de Clientes (POO) ===")
        print("1. Adicionar Novo Cliente")
        print("2. Listar Clientes Cadastrados")
        print("3. Remover Cliente") 
        print("9. Sair do Sistema")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            nome, idade, cidade = _obter_dados_cliente()
            if nome:
                sistema.adicionar_cliente(nome, idade, cidade)
        elif opcao == '2':
            sistema.listar_clientes()
        elif opcao == '3':
            _remover_cliente(sistema)
        elif opcao == '9':
            sistema.salvar_dados()
            print("\nObrigado por usar o sistema POO! Encerrando...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida do menu.")

if __name__ == "__main__":
    menu_principal()