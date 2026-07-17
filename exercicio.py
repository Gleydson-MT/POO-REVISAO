class Aluno:
    contador = 0
    def __init__(self, nome):
        self.nome = nome
        Aluno.contador += 1
        
aluno1= Aluno("Alisson")
aluno2 = Aluno("Thiago")

print(Aluno.contador)
