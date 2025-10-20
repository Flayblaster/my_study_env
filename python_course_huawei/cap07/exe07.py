"""
Escreva um programa que leia um número inteiro nA e gere uma lista A com nA valores inteiros
aleatórios, não repetidos e situados na faixa [1, 100]. Mostre-a na tela em ordem crescente.
Em seguida leia outro inteiro nB e gere a lista B usando as mesmas regras aplicadas à lista A. Mostrea na tela também em ordem crescente.
Crie e exiba uma lista contendo a união das listas A e B, sem conter valores repetidos. Mostre a lista
resultante e a quantidade de elementos dela.
Exemplo: nA = 7 lista A = [8, 12, 29, 35, 44, 64, 81]
nB = 5 lista B = [10, 25, 35, 38, 64]
Saída: União de A e B
[8, 10, 12, 25, 29, 35, 38, 44, 64, 81] contém 10 elementos
"""
from random import randint

lista_A = []
qtde = int(input('Número de elementos: '))
for _ in range(qtde):
    num = randint(1, 100)
    while num in lista_A:
        num = randint(1, 100)
    else:
        lista_A.append(num)

lista_A.sort()
print(lista_A)

lista_B = []
qtde = int(input('Número de elementos: '))
for _ in range(qtde):
    num = randint(1, 100)
    while num in lista_B:
        num = randint(1, 100)
    else:
        lista_B.append(num)

lista_B.sort()
print(lista_B)

lista_C = lista_A[:]
for item in lista_B:
    if not item in lista_C:
        lista_C.append(item)
    else:
        continue

lista_C.sort()
print(lista_C)