"""
Escreva um programa que permaneça que leia um arquivo de entrada, sabendo que esse arquivo
tem um número inteiro em cada linha. Todos os números lidos devem ser mostrados na tela. Mostrar
também a soma dos valores, a quantidade, a média aritmética, o menor valor e o maior valor. Usar
aqui o mesmo arquivo de entrada do exercício anterior.
"""
# declaração de variáveis
lista = list()
soma = count = 0

for linha in open('arq_exe04_cap11.txt'): # adiciona as linhas do arq na lista
    lista.append(int(linha))

for item in lista: #Cálcula a soma e a contagem dos dados
    soma += item
    count += 1

#Apresenta as informações na tela
print(lista)
print(f'Soma dos Valores: {soma}')
print(f'COntagem dos valores: {count}')
print(f'Média aritimética dos valores: {soma/count}')
print(f'Menor valor da lista: {min(lista)}')
print(f'Maior valor da lista: {max(lista)}')

