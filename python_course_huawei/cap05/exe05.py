"""
Escreva um programa que leia três números inteiros: LMin, LMax e D. Em seguida exiba na tela todos
os valores divisíveis por D que estão dentro do intervalo fechado [LMin, LMax].
"""

Lmin = int(input('Valor inicial: '))
Lmax = int(input('valor final: '))+1
D = int(input('Dividendo: '))


while Lmin != Lmax:
    if (Lmin%D) == 0:
        print(Lmin)
    Lmin += 1