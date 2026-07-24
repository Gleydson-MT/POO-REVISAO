from abc import ABC, abstractmethod

# super classe funcionario
class Funcionario(ABC):
    def __init__(self, cpf, nome, matricula, salario_basico):
        self.cpf = cpf
        self.nome = nome
        self.matricula = matricula
        self.salario_basico = salario_basico
    @abstractmethod
    def calcular_salario(self):
        pass

class Vendendor(Funcionario):
    def __init__(self, cpf, nome, matricula, salario_basico, comissao):
        super().__init__(cpf, nome, matricula, salario_basico)
        self.comissao = comissao
        self.venda_mes = 0
        self.venda = {} #Chave: valor sendo a chave "DATA";"ACMULADO DE VENDA DO MÊS"
    def calcular_salario(self, data_salario):
        if data_salario in self.vendas:
            self.venda_mes = self.vendas
        return self.calcular_salario + (self.venda_mes * self.comissao)

    def add_venda(self, valor_venda, data):
    #MM/AAAA
        if data not in self.venda:
            self.venda[data] = 0
        self.venda[data] += valor_venda


class Gerente(Funcionario):
    def __init__(self, cpf, nome, matricula, salario_basico, bonus):
        super().__init__(cpf, nome, matricula, salario_basico)
        self.bonus = bonus

    def calcular_salario(self):
        return self.calcular_salario() + self.bonus

class Estagiario(Funcionario):
    def __init__(self, cpf, nome, matricula, salario_basico, carga_horaria):
        super().__init__(cpf, nome, matricula, salario_basico)
        self.carga_horario = carga_horaria

    def calcular_salario(self):
        return super().calcular_salario()