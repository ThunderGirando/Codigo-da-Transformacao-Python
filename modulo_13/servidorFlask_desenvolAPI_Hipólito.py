import sqlite3
from flask import Flask, request, jsonify

DB_NAME = 'modulo_13/usuarios.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        );
    ''')
    conn.commit()
    conn.close()

init_db()

app = Flask(__name__)

@app.route('/saudacao', methods=['GET'])
def saudacao():
    return jsonify({"mensagem": "Olá! Bem-vindo à sua API Flask."}), 200

@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    if not request.is_json:
        return jsonify({"erro": "O corpo da requisição deve ser JSON"}), 400

    dados = request.get_json()
    nome_usuario = dados.get('nome')

    if not nome_usuario:
        return jsonify({"erro": "O campo 'nome' é obrigatório no JSON"}), 400

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO usuarios (nome) VALUES (?)", (nome_usuario,))
        conn.commit()

        novo_id = cursor.lastrowid

        conn.close()

        return jsonify({
            "mensagem": "Usuário cadastrado com sucesso!",
            "id": novo_id,
            "nome": nome_usuario
        }), 201

    except Exception as e:
        return jsonify({"erro": f"Erro ao persistir dados: {str(e)}"}), 500

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("SELECT id, nome FROM usuarios")
        usuarios = cursor.fetchall()
        
        conn.close()

        usuarios_list = [{"id": u[0], "nome": u[1]} for u in usuarios]

        return jsonify({"usuarios": usuarios_list}), 200
    
    except Exception as e:
        return jsonify({"erro": f"Erro ao buscar dados: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)