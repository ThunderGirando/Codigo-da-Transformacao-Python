import json

def test_rota_ola_sucesso(client):
    response = client.get('/ola')

    assert response.status_code == 200
    dados = json.loads(response.data.decode('utf-8')) 
    assert dados['mensagem'] == "Olá, Mundo! API está funcionando."
    assert response.content_type == 'application/json'


def test_rota_soma_sucesso(client):
    dados_requisicao = {"a": 15, "b": 7}
    
    response = client.post(
        '/soma',
        data=json.dumps(dados_requisicao),
        content_type='application/json'
    )


    assert response.status_code == 200
    dados = json.loads(response.data.decode('utf-8'))
    assert dados['resultado'] == 22.0


def test_rota_soma_erro_dados_ausentes(client):
    dados_requisicao = {"a": 10}
    
    response = client.post(
        '/soma',
        data=json.dumps(dados_requisicao),
        content_type='application/json'
    )

    assert response.status_code == 400
    dados = json.loads(response.data.decode('utf-8'))
    assert 'erro' in dados
    assert dados['erro'] == "Requisição inválida. Forneça 'a' e 'b'."