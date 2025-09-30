"""
Escreva um programa que leia um número N e em seguida exiba na tela todos os números divisíveis
por 7 entre 1 e N (inclusive).
"""
while True:
    n = int(input('Digite um número: '))
    if n == 0:
        break
    elif (n%7) == 0:
        print(f'{n} é divisível por 7')
    else:
        print(f'{n} não é divisível por 7')
