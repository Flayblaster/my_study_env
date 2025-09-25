"""Escreva um programa que leia o nome de um aluno e as notas obtidas em três avaliações. A média
final é a média aritmética das três notas e a pessoa estará aprovada se essa média for maior ou igual
a 7,0. Mostre na tela o nome, a média e a situação que será 'Aprovado' ou 'Reprovado'"""

aluno = str(input('Nome do aluno: '))
nota1 = float(input('Nota da 1ºAvaliação: '))
nota2 = float(input('Nota da 2ºAvaliação: '))
nota3 = float(input('Nota da 3ºAvaliação: '))

media = (nota1+nota2+nota3)/3

if media >= 7.0:
    print(f'Aluno {aluno} aprovado!!')
    print(f'Média do aluno: {media:.2f}')
else:
    print(f'Aluno {aluno} reprovado!!')
    print(f'Média do aluno: {media:.2f}')