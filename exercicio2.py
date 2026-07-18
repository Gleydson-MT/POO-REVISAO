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


class Quadrado:
    objeto = "Quadrado"
    def __init__(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado

    def saudacao(self):
        print(f"O quadrado mede {self.tamanho_do_lado}, metros quadrados.")
        pass