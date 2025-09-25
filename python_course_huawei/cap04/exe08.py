"""
Escreva um programa que leia um número inteiro que representa um ano. Informe se esse ano é
bissexto ou não.
O ano é bissexto se cumprir uma das seguintes condições:
a) ser múltiplo de 4 e ao mesmo tempo não ser múltiplo de 100
b) ser múltiplo de 400
"""

ano = int(input('Ano: '))

if ((ano%4) == 0 and not (ano%100) == 0) or (ano%400) == 0:
    print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto')
