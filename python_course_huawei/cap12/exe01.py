"""
Escreva um programa que leia dois números reais e calcule as 4 operações aritméticas entre eles
usando uma função. Exiba o resultado com duas casas decimais.
"""

def all_op(num1: float, num2: float) -> tuple:
    """
    Faz soma, subtração, divisão, multiplicação, de 2 valores.
    -> num1: int
    -> num2: int
    -> return: Todos os objetos utilizados em uma tupla
    """
    soma = num1 + num2
    sub = num1 - num2
    div = num1 / num2
    mult = num1 * num2

    return soma, sub, div, mult

# Recebe a entrada do usuário, para os dois valores usados
num1 = float(input('1º Número: '))
num2 = float(input('2º Número: '))
result = all_op(num1, num2) #chama a função

# apresenta o resultado para o usuário
print('Resultado')
print(f'SOMA = {result[0]:.2f}')
print(f'SUBTRAÇÃO = {result[1]:.2f}')
print(f'DIVISÃO = {result[2]:.2f}')
print(f'MULTIPLICAÇÃO = {result[3]:.2f}')

