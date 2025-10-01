"""
Escreva um programa que leia dois números inteiros: LMin e LMax. Em seguida exiba na tela todos
os valores dentro do intervalo fechado [LMin, LMax].
"""

lmin = int(input('valor inicial: '))
lmax = int(input('valor final: '))
print(lmin)

while lmin != lmax:
    lmin += 1
    print(lmin)