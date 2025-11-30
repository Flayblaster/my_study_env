"""
Escreva um programa que leia um arquivo CSV de entrada que tenha dois inteiros em
cada linha. O primeiro é um código de produto e o segundo é a quantidade vendida. O
programa deve totalizar quantos itens foram vendidos para cada produto.
Dica: use um dicionário tendo o código como chave e a quantidade como valor. Para
cada código lido do arquivo verifique se ele já existe no dicionário usando o operador
in. Se não existir, inclua; se existir some a quantidade existente com a nova quantidade
lida do arquivo.
"""
from collections import defaultdict

total = dict()
soma = 0

arq = open('arq_exe09_cap11.txt', 'r')
linhas = arq.readline()

while linhas != '':
    linhas = linhas.strip().split(';')
    if linhas[0] not in total:
        total[linhas[0]] = int(linhas[1])
    else:
        total[linhas[0]] += int(linhas[1])
    linhas = arq.readline()

print(total)