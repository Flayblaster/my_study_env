"""Escreva um programa que leia a idade de uma pessoa e indique qual sua classe eleitoral:
a) menor que 16 anos -> não eleitor
b) entre 18 completos e 65 anos incompletos -> eleitor obrigatório
c) entre 16 anos completos e 18 anos incompletos ou 65 anos completos -> eleitor facultativo"""

idade = int(input('Sua idade: '))

if idade < 16:
    print('Não eleitor')
elif 65 > idade >= 18:
    print('Eleitor obrigatório')
else:
    print('Eleitor facultativo')