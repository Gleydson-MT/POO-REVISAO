from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, placa, marca, modelo, ano):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    @abstractmethod
    def calcular_custo(self, km):
        pass

class Onibus(Veiculo):
    def __init__(self, placa, marca, modelo, ano_de_fabricacao, capacidade_passageiro):
        super().__init__(placa, marca, modelo, ano_de_fabricacao)
        self.capacidade_passageiro = capacidade_passageiro

    def calcular_custo(self, km):
        return km * 5

class Taxi(Veiculo):
    def __init__(self, placa, marca, modelo, ano_de_fabricacao, bandeirada):
        super().__init__(placa, marca, modelo, ano_de_fabricacao)
        self.bandeirada = bandeirada

    def calcular_custo(self, km):
        return self.bandeirada + km * 2.5

class Caminhao(Veiculo):
    def __init__(self, placa, marca, modelo, ano_de_fabricacao, capacidade_carga):
        super().__init__(placa, marca, modelo, ano_de_fabricacao)
        self.capacidade_carga = capacidade_carga

    def calcular_custo(self, km):
        return self.capacidade_carga + km * 8