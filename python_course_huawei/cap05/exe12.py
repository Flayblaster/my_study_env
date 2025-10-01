"""
Escreva um programa que leia dois inteiros: Qtde e Prim. Em seguida mostre na tela os Qtde termos
da sequência de Fibonacci que sejam maiores que Prim.
"""

qtde = int(input('Quantidade: '))
prim = int(input('Inicio: '))

a = c = count = 0
b = 1
while count != qtde+prim:
    if a >= prim:
        print(a)
    count += 1
    c = a + b
    a = b
    b = c
