class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_dados(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")


carro1 = Carro("Toyota", "Corolla")
carro1.exibir_dados()

carro2 = Carro("Honda", "Civic")
carro2.exibir_dados()
