"""
Escreva um programa que leia uma quantidade Qtde e mostre na tela os Qtde primeiros termos da
sequência de Fibonacci.
A sequência de Fibonacci é definida da seguinte forma: a) os dois primeiros termos da sequência
são 0 e 1. Do terceiro termo em diante cada termo é a soma dos dois anteriores.
Caso de teste: Se Qtde = 9, então a sequência é: 0, 1, 1, 2, 3, 5, 8, 13, 21
"""

qtde = int(input('Quantidade de valores: '))
count = 0
a = c = 0
b = 1
while count != qtde:
    print(a)
    count += 1
    c = a + b
    a = b
    b = c
