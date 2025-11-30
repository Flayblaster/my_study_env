"""
Escreva um programa que leia o arquivo NUMEROS.TXT gerado no exercício proposto 11.4,
colocando-os em uma lista. Ordene a lista usando o .sort() e grave os números ordenados no arquivo
ORDENADOS.TXT.
"""
# declaração de variáveis
arq = open('numeros.txt', 'r+')
lista = []

for item in arq.readlines():
    lista.append(int(item))
arq.close()
lista.sort()

arq = open('ordenados.txt', 'w')
for item in lista:
    arq.write(f'{item}\n')

arq.close()