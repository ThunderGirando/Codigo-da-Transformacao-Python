class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_dados(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")

class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Autonomia da Bateria: {self.autonomia_bateria} km")


carro_eletrico = CarroEletrico("Tesla", "Model S", 600)
carro_eletrico.exibir_dados()
