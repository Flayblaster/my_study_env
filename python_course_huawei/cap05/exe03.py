"""
Escreva um programa que obrigatoriamente leia um inteiro que esteja no intervalo fechado
[100, 200]. Se o valor fornecido estiver fora do intervalo o programa deve avisar que o valor é inválido
e permanecer no laço. Quando um valor válido for fornecido o programa deve informar que o valor
foi aceito e terminar
"""

num = int(input('Digite um número: '))
while not (100 <= num <= 200):
    print('Valor inválido')
    num = int(input('Digite um número: '))
else:
    print('Valor válido')