"""
Escreva um programa que leia e armazene em um dicionário os seguintes dados dos seus contatos:
nome, número celular, email e data de aniversário.
A chave deve o nome. O valor deve ser um dicionário aninhado contendo os demais dados. Se o
nome já existir no dicionário o programa deve perguntar se o usuário deseja alterar o cadastro.
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
    contratos[nome] = {"Número de Celular": num_cel, "Email": email, "Data de Nascimento": bthd}

contratos_sort = sorted(contratos.items())
contratos_sorted = dict(contratos_sort)
print(f'{'Nome':20} {'Celular':20} {'Email':20} {'Data de Aniversário':>30}')
for nome, info in contratos_sorted.items():
    print(f'{nome:20} {info['Número de Celular']:20} {info['Email']:20} {info['Data de Nascimento']:>21}')
