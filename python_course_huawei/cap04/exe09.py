"""
Escreva um programa que leia 3 números inteiros e mostre na tela uma das seguintes opções:
a) 'Os três valores são iguais'
b) 'Há dois valores iguais e um diferente'
c) 'Os três valores são diferentes'
"""

int1 = int(input('1º Número: '))
int2 = int(input('2º Número: '))
int3 = int(input('3º Número: '))

if int1 == int2 == int3:
    print('Os três são iguais')
elif int2 == int1 or int3 == int1 or int2 == int3:
    print('Dois deles são iguais')
else:
    print('Todos são difirentes')