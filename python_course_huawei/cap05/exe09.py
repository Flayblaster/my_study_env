"""
Escreva um programa que leia um número inteiro N. Em seguida calcule e mostre na tela o fatorial
de N (N!).
"""
f = 1
i = 0
n = int(input('Número: '))
while i != n:
    i += 1
    f *= i
print(f'O fatorial desse valor ({n}) é {f}')