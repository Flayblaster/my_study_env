"""
Escreva um programa que leia um arquivo de entrada contendo números inteiros, sendo um por
linha, e os coloque em uma lista. Em seguida pense em alguma forma de remover os valores
repetidos, deixando apenas uma cópia de cada valor.
A lista resultante após a eliminação dos repetidos, deve ser ordenada e salva no arquivo
UNICOS.TXT, um inteiro por linha.
"""
# declaração de variáveis
arq = open('ordenados.txt', 'r')
arq2 = open('unicos.txt', 'w')
lista = []
item_ant = ''

# a iteração lê um item do arq e compara com o item anterior.
for item in arq.readlines():
    if not item in lista:
        lista.append(item)
arq2.writelines(lista)

arq.close()
arq2.close()