class Cadastro:
    salão = "Cliente"
    def __init__(self, nome, cpf, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
    def __str__(self):
        return f"\n{self.nome}- CPF:{self.cpf}\nTelefone:{self.telefone}\nE-mail:{self.email}\n Registro realizado com sucesso!\n"

while True:
    print("=== SISTEMA DE CADASTRO ===")
    print("[1] Cadastra cliente.")
    print("[0] Sair")
    op = input("Digite a opção desejada: ")

    if op == "1":
        nome = input("Digite o nome do cliente: ")
    while True:
        cpf = int(input("Digite o CPF do cliente: "))
        if cpf == "":
            print("Preencha o campo acima para continuar.")
        elif len(cpf) != 11:
            print("""Quantidade de dígitos fora do padrão.""")
        elif not cpf.isdigit():
            print("Caracteres fora do padrão suportado.")
        elif cpf_exist(cpf):
            print("CPF já cadastrado. Tente outro número.")
        else:
            break
        telefone = int(input("Digite o telefone do cliente: "))
        email = input("Informe o E-mail do cliente: ")
        input("Digite qualquer tecla para continuar.")
# elif op == "0":
# print("Saindo do sistema...")
# break
