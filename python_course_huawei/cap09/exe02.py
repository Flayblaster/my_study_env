"""
Escreva um programa que leia do teclado dois conjuntos de números inteiros digitados pelo usuário.
Exiba na tela a união e a interseção desses conjuntos.
"""
from random import randint

conj1 = set()
conj2 = set()

def num_gen(conjunto, qtde):
    counter = 0
    while qtde != counter:
        num = randint(1, 50)
        if num in conjunto:
            continue
        else:
            conjunto.add(num)
            counter += 1

num_gen(conj1, int(input('Quantidade do 1º conjunto: ')))
num_gen(conj2, int(input('Qauntidade do 2º Conjunto: ')))

print(f'Conjunto 1: {conj1}')
print(f'Conjunto 2: {conj2}')
print(f'União dos conjuntos: {conj1|conj2}')
print(f'interseção dos conjuntos: {conj1&conj2}')
