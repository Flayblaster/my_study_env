"""
Reescreva o programa exercício resolvido 11.6 usando um dicionário aninhado no lugar da tupla
como valor para o dicionário Estoque.
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