"""
Escreva um programa que leia e armazene em um dicionário os seguintes dados dos seus contatos:
nome, número celular, email e data de aniversário.
A chave deve o nome. O valor pode ser uma tupla ou um dicionário aninhado. Você escolhe.
Ao digitar um string vazio para o nome, o programa interrompe a leitura e apresente todos dados na
tela na mesma formatação dos exercícios anteriores.
Neste exercício os nomes devem estar em ordem alfabética.
Use a função sorted() de Python.
"""

contatos = dict()

while True:
    nome = str(input('Nome: '))
    if nome in '':
        print('Programa Finalizado')
        break
    num_cell = str(input('Número: '))
    email = str(input('Email: '))
    bthd = str(input('Data de Nascimento: '))
    contatos[nome] = (num_cell, email, bthd)

contatos_sort = sorted(contatos.items())
contatos_sorted = dict(contatos_sort)

for nome, info in contatos_sorted.items():
    print(nome, info)
