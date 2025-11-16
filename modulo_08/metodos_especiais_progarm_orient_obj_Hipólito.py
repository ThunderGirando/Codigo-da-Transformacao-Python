class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        print(f"Carro {self.marca} {self.modelo} inicializado!")

    def __str__(self):
        return f"Carro: {self.marca} {self.modelo}"

# Exemplo de uso
carro1 = Carro("Toyota", "Corolla")
print(carro1)

carro2 = Carro("Honda", "Civic")
print(carro2)
