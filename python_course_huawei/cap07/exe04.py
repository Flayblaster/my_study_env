from random import randint
"""
Escreva um programa que leia um número inteiro Qtde e carregue uma lista com essa quantidade
de números inteiros aleatórios quaisquer. Exiba a lista na tela.
Em seguida verifique se existem e elimine valores que estiverem repetidos, deixando apenas uma
ocorrência de cada. A ordem relativa dos elementos na lista não deve ser alterada, com exceção às
consequências da eliminação dos repetidos. Exiba a nova lista sem repetidos e o seu tamanho.
"""
qtde = int(input('Entrada: '))
lista = []
for _ in range(qtde):
    num = randint(0, 1000)
    while num in lista:
        num = randint(0, 1000)
    lista.append(num)
print(lista)
print('Tamanho da lista:', len(lista))