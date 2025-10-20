"""
Altere a solução do ex.resolvido 7.3 para exibir os números reais da lista com duas casas decimais.

Escreva um programa que leia um número inteiro N. Em seguida leia N números reais carregando os numa lista.
Ao final exiba os elementos da lista na tela, sendo um em cada linha
"""
qtd = int(input('Quantidade de números: '))
lista = []
for _ in range(qtd):
    entrada = float(input('Número: '))
    lista.append(entrada)
for x in lista:
    print(f'{x}:.2f')
