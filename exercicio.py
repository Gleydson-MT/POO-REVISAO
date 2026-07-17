class Aluno:
    escola = "Senac"
    contador = 0
    def __init__(self, nome):
        self.nome = nome
        Aluno.contador += 1
        print(f"O aluno {self.nome} criado com sucesso, agora temos {Aluno.contador} alunos criados!")

        
aluno1 = Aluno("Thiago")
aluno2 = Aluno("Alisson")
