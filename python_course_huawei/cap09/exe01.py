"""
Escreva um programa que leia um inteiro Qtde e crie um conjunto com elementos numéricos inteiros
aleatórios dentro do intervalo fechado [1, 50]. Mostre o conjunto gerado na tela.
Lembre-se que os conjuntos não podem ter elementos repetidos, então a geração de números
aleatórios pode representar um problema. Como resolver isso?
"""
from random import randint

qtde = int(input('Quantidade: '))
conjunto = set()

while len(conjunto) < qtde < 50:
    num = randint(1, 50)
    if num in conjunto:
        continue
    else:
        conjunto.add(num)
else:
    print('Quantidade inválida')

print(conjunto)