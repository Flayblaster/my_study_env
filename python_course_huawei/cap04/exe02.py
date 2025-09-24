"""Escreva um programa que leia um número inteiro e mostre na tela se ele é divisível por 10 ou não.
"""
num = int(input('Número: '))
resp = num%10

if resp == 0:
    print(f'Esse valor ({num}) é divisível por 10')
else:
    print(f'Esse valor ({num}) não é divisível por 10')