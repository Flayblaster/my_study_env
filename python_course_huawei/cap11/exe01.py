"""
Escreva um programa que permaneça em laço lendo números inteiros até que seja digitado 0. Todos
os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha.
Usar o mélodo .write()
"""

arq = open('arq_exe01_cap11.txt', 'w') #Abre o arq "arq_ex01_cap.txt"
num = int(input('Número: '))

while num != 0: #Escreve em linha separadas a entrada do usuário
    arq.write(f'{num}\n')
    num = int(input('Número: '))
arq.close()
print('fim')