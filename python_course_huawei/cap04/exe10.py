"""
Escreva um programa que leia 3 números inteiros e mostre na tela se eles formam um triângulo ou
não. Caso formem um triângulo informe o tipo de triângulo (equilátero, isósceles ou escaleno).
Para três números formarem um triângulo precisa ocorrer que:
a) os três números precisam ser maiores que zero;
b) a soma dos dois menores valores deve ser maior que o terceiro.
"""

num1 = float(input('1º Número: '))
num2 = float(input('2º Número: '))
num3 = float(input('3º Número: '))
sortedlist = [num1, num2, num3]
sortedlist.sort()
print(sortedlist)
if not (num1 <= 0 or num2 <= 0 or num3 <= 0):
    if sortedlist[2] <= (sortedlist[0] + sortedlist[1]):
        if num1 == num2 == num3:
            print('Com esses valores você vai formar um triângulo equilátero')
        elif num1 == num2 or num2 == num3 or num3 == num1:
            print('Com esses valores você vai formar um triângulo isósceles')
        else:
            print('Com esses valores você vai formar um triângulo escaleno')
    else:
        print('A soma dos dois menores valores são menores que o terceiro valor')
else:
    print(f'{num1, num2, num3} Esses valores não formam um triângulo')
    