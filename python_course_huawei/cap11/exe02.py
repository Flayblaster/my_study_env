"""
Escreva um programa que permaneça em laço lendo números reais até que seja digitado 0. Todos
os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha, com
3 casas decimais. Usar o método .write()
"""

arq = open('arq_exe02_cap11.txt', 'w') #abre o arquivo "arq_exe02_cap11.txt
num = float(input('Número: ')) #primeira entrada do usuário

while num != 0: #Le a entrada do usuário e escreve no arquivo, até que a entrada seja 0
    arq.write(f'{num:.3f}\n')
    num = float(input('Número: '))
arq.close()
print('Fim')