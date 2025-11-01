"""
Escreva um programa para uma fábrica de calçados que leia o código LL de um calçado, que é um
número inteiro com 2 dígitos. Exiba na tela a linha do calçado, conforme a tabela a seguir. Se o
número fornecido não estiver na tabela, deve-se exibir a mensagem "Código inválido"
"""
from fontTools.misc.textTools import caselessSort

ll = int(input('Código: '))
match ll:
    case 16:
        print('Bebê')
    case 23:
        print('Infantil feminino')
    case 25:
        print('Infantil masculino')
    case 29:
        print('Infantil esportivo')
    case 42:
        print('Masculino normal')
    case 43:
        print('Masculino casual')
    case 49:
        print('Masculino esportivo')
    case 52:
        print('Feminino formal salto baixo')
    case 53:
        print('Feminino formal salto alto')
    case 55:
        print('Feminino csual salto baixo')
    case 56:
        print('Feminino casual salto alto')
    case 59:
        print('Feminino esportivo')
    case _:
        print('Código inválido')
