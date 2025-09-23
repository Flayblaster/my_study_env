'''Escreva um programa que leia um número real e mostre na tela os valores de 25%, 50%, 75% do
valor lido usando o formato com 3 casas decimais mostrado abaixo:'''

num_real = float(input('digite um número: '))
nr_25 = num_real*0.25
nr_50 = num_real*0.50
nr_75 = num_real*0.75

print(f'25% de {num_real} = {nr_25:.3f}')
print(f'50% de {num_real} = {nr_50:.3f}')
print(f'75% de {num_real} = {nr_75:.3f}')