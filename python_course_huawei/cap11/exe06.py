"""
Escreva um programa que leia um arquivo de entrada carregando seus dados em um dicionário e ao
final exibindo-os na tela. A figura 11.1 mostra o do lado esquerdo a natureza dos dados que serão
lidos e do lado direito mostra o formato do arquivo.
Esse formato é conhecido como CSV. Arquivos CSV são muito usados em diversas áreas da
computação, em especial em Análise de Dados. O que caracteriza um arquivo CSV é que cada linha
tem um conjunto de dados de alguma forma relacionados e separados por um caractere
delimitador. No arquivo deste exercício o delimitador é um ponto-e-vírgula ";"
Neste caso, cada linha tem: código de produto (int), a quantidade em estoque (int), preço (float).
Use o código como chave para o dicionário e valor deve ser em formato de tupla.
"""
# declaração de variáveis
lista = dict()
soma = 0
arq = open('arq_exe06_cap11.txt', 'r') # abre o arq usado no programa


for line in arq: # lê as linhas do arq e trata elas para virarem dicionários
    item = line.strip().split(';')
    lista[item[0]] = item[1:3]

# exibição das info no console
print(lista)
print('Exibição dos dados na forma de tabela')
for cod, info in lista.items(): # apresenta as info em formato de tabela
    res = int(info[0])*float(info[1])
    soma += res
    print(f'{cod:4}: {info[0]:>3} x {info[1]:5} = {res:5.2f}')
print(f'{soma:>28.2f}')