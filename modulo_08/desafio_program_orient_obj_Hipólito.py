import json
import os

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"Livro: {self.titulo} - Autor: {self.autor} - Status: {status}"

    def to_dict(self):
        return {
            'titulo': self.titulo,
            'autor': self.autor,
            'disponivel': self.disponivel
        }

    @classmethod
    def from_dict(cls, data):
        livro = cls(data['titulo'], data['autor'])
        livro.disponivel = data['disponivel']
        return livro

class Biblioteca:
    def __init__(self):
        self.livros = {}  
        self.carregar_biblioteca()

    def adicionar_livro(self, livro):
        self.livros[livro.titulo] = livro
        self.salvar_biblioteca()

    def listar_livros_disponiveis(self):
        disponiveis = [livro for livro in self.livros.values() if livro.disponivel]
        if not disponiveis:
            print("Nenhum livro disponível.")
        else:
            for livro in disponiveis:
                print(livro)

    def emprestar_livro(self, titulo):
        if titulo in self.livros and self.livros[titulo].disponivel:
            self.livros[titulo].disponivel = False
            print(f"Livro '{titulo}' emprestado.")
            self.salvar_biblioteca()
            return True
        print("Livro não encontrado ou já emprestado.")
        return False

    def devolver_livro(self, titulo):
        if titulo in self.livros and not self.livros[titulo].disponivel:
            self.livros[titulo].disponivel = True
            print(f"Livro '{titulo}' devolvido.")
            self.salvar_biblioteca()
            return True
        print("Livro não encontrado nos empréstimos.")
        return False

    def salvar_biblioteca(self):
        data = {titulo: livro.to_dict() for titulo, livro in self.livros.items()}
        with open('modulo_08/biblioteca.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def carregar_biblioteca(self):
        if os.path.exists('modulo_08/biblioteca.json'):
            with open('modulo_08/biblioteca.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.livros = {titulo: Livro.from_dict(livro_data) for titulo, livro_data in data.items()}


biblioteca = Biblioteca()


print("Livros disponíveis:")
biblioteca.listar_livros_disponiveis()


