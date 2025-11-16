
with open('modulo_06/info.txt', 'w') as arquivo:
    arquivo.write("Nome: Hipólito\n")
    arquivo.write("Idade: 25\n")
    arquivo.write("Cidade: São Paulo\n")

print("Arquivo criado e informações escritas.")

with open('modulo_06/info.txt', 'r') as arquivo:
    conteudo = arquivo.read()

print("\nInformações lidas do arquivo:")
print(conteudo)
