class Bola:
    objeto = "Bola"
    def __init__(self, cor, circunferencia, materia):
        self.cor = cor
        self.circunferencia = circunferencia
        self.materia = materia

    def saudacao(self):
        print(f"A {self.objeto}, possui a cor {self.cor}, de circunferencia do tamanho {self.circunferencia}, feita de {self.materia}.")

bola1 = Bola("Branca", 30, "Plastico")

bola1.saudacao()

class Calculadora:
    def multiplicar(self, a, b):
        return a*b
calc = Calculadora()

class Quadrado:
    lados = 2
    # objeto = "Quadrado"
    # soma_de_lados = 0
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def saudacao(self):
        print(f"O quadrado mede {calc.multiplicar(self.a, self.b)} metros quadrados.")

quadrado1 = Quadrado(10, 30)
quadrado1.saudacao()