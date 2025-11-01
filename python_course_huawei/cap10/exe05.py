"""
Considere o seguinte conjunto de dados: Nome + (N1, N2, N3, N4). Nome representa o nome de um
aluno e deve ser usado como chave. N1, N2, N3, N4 representam as notas de provas desse aluno.
Escreva um programa que leia os dados de Q alunos e determine a situação de cada aluno. O critério
que garante a aprovação é que a média aritmética das 4 notas de prova seja maior ou igual 6,0. Q é
a quantidade de alunos e este valor deve ser lido do teclado no começo do programa.
Para cada aluno o nome deve ser lido em separado e suas notas de prova devem ser lidas juntas na
mesma linha, com um espaço em branco de separação.
Para cada aluno o programa deve mostras o Nome, as 4 notas de prova, a média final e a situação
(aprovado/reprovado). As notas devem ser exibidas com uma casa decimal.
"""
counter = media = 0
qtde_alunos = int(input('Quantidade de alunos: '))
alunos = dict()

while qtde_alunos != counter:
    Nome = str(input('Nome do aluno: ')).title()
    notas = input('Notas: ')
    notas = notas.split()
    alunos[Nome] = notas
    counter += 1

for nome, notas in alunos.items():
    media = 0
    soma = 0
    for nota in notas:
        soma += float(nota)
    media = soma/4
    print(f'Nome do aluno: {nome}, Média aritmética: {media}')
