"""
Escreva um programa que permaneça que leia um arquivo de entrada, sabendo que esse arquivo
tem um número inteiro em cada linha. Todos os números lidos devem ser mostrados na tela. Mostrar
também a soma dos valores, a quantidade, a média aritmética, o menor valor e o maior valor.
"""
arq = open('arq_exe04_cap11.txt', 'r')


# declaração de variáveis
soma = count = 0
lista = list()
linha = arq.readline()

while linha != '': # Adiciona as linhas a lista e cálcula a soma e qtd dos valores
    lista.append(int(linha))
    soma += int(linha)
    count += 1
    linha = arq.readline()
arq.close()
lista.sort()

# apresenta os dados no console
print(lista)
print(f'Soma dos Valores: {soma}')
print(f'COntagem dos valores: {count}')
print(f'Média aritimética dos valores: {soma/count}')
print(f'Menor valor da lista: {min(lista)}')
print(f'Maior valor da lista: {max(lista)}')