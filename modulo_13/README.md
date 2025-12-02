# Ao executar o arquivo servidorFlask... (no terminal) você tera que abrir outro terminal e testar com os comandos

(GETs)
1. curl http://127.0.0.1:5000/saudacao
2. curl http://127.0.0.1:5000/usuarios

(POST)
1. curl -X POST -H "Content-Type: application/json" -d '{"nome": "Fulano da Silva"}' http://127.0.0.1:5000/cadastrar