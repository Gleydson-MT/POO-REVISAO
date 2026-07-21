class Cadastro:
    salão = "Cliente"
    def __init__(self, nome, cpf, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
    def __str__(self):
        return f"\n{self.nome}- CPF:{self.cpf}\nTelefone:{self.telefone}\nE-mail:{self.email}\n Registro realizado com sucesso!\n"

class Serviços:
    def __init__(self, nome, valor, duracao):
        self.nome = nome
        self.valor = valor
        self.duracao = duracao
        pass

while True:
    print("""  ======== SISTEMA DE CADASTRO ========
          1. Cadastra Cliente
          2. Cadastra Serviço
          3. Agendar Atendimento
          4. Listar Agendamentos
          5. Cancelar Agendamento
          0. Sair
    """)

    
    
    op = input("Digite a opção desejada: ")

    if op == "1":
        while True:
            nome = input("Digite o nome do cliente: ")
            if nome == "":
                print("Preencha o campo acima")
            else:
                break
        while True:
            cpf = (input("Digite o CPF do cliente: "))
            if cpf == "":
                print("Preencha o campo acima para continuar.")
            elif len(cpf) != 11:
                print("""Quantidade de dígitos fora do padrão.""")
            elif not cpf.isdigit():
                print("Caracteres fora do padrão suportado.")
            else:
                break
        telefone = int(input("Digite o telefone do cliente: "))
        email = input("Informe o E-mail do cliente: ")
        input("Digite qualquer tecla para continuar.")