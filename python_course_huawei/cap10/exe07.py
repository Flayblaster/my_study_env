"""
Escreva um programa que leia e armazene em um dicionário os seguintes dados dos seus contatos:
nome, número celular, email e data de aniversário.
A chave deve ser o nome. O valor deve ser uma tupla contendo os demais dados. Se o nome já
existir no dicionário o programa deve perguntar se o usuário deseja alterar o cadastro.
Ao digitar um string vazio para o nome, o programa interrompe a leitura. Antes de encerrar o programa
apresente os dados em um formato de tabela.
"""

contratos = dict()
while True:
    nome = str(input('Nome: '))
    if nome in '':
        print('Programa Finalizado!!')
        break
    elif nome in contratos:
        resp = str(input('Esse nome já existe, deseja alterá-lo?'))
        if resp in 's':
            nome_new = str(input('Novo nome: '))
            contratos[nome_new] = contratos[nome]
            contratos[nome].pop()
            print('Nome alterado!!')
    num_cel = str(input('Número de celular: '))
    email = str(input('Email: '))
    bthd = str(input('Data de Aniversário (dd/mm/yyyy): '))
    contratos[nome] = (num_cel, email, bthd)

contratos_sort = sorted(contratos.items())
contratos_sorted = dict(contratos_sort)
print(f'{'Nome':20} {'Celular':20} {'Email':20} {'Data de Aniversário':>30}')
for nome, info in contratos_sorted.items():
    print(f'{nome:20} {info[0]:20} {info[1]:20} {info[2]:>21}')
