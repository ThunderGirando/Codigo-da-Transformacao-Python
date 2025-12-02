#py -m pytest test_api.py 
 
#python -m pytest test_api.py

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/ola', methods=['GET'])
def ola_mundo():
    return jsonify({"mensagem": "Olá, Mundo! API está funcionando."}), 200

@app.route('/soma', methods=['POST'])
def somar_numeros():

    dados = request.get_json()
    
    # Validação básica
    if not dados or 'a' not in dados or 'b' not in dados:
        return jsonify({"erro": "Requisição inválida. Forneça 'a' e 'b'."}), 400

    try:
        a = float(dados['a'])
        b = float(dados['b'])
        resultado = a + b
        
        return jsonify({"resultado": resultado}), 200
    except ValueError:
        return jsonify({"erro": "Valores de 'a' e 'b' devem ser números."}), 400

if __name__ == '__main__':
    app.run(debug=True)