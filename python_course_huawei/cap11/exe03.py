"""
Escreva um programa que permaneça em laço lendo números reais até que seja digitado 0. Todos
os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha, com
três casas decimais. Usar o método .writelines()
"""
#declaração de variáveis
lista = list()

arq = open('arq_exe03_cap11.txt', 'w') #Abre o arquivo
num = int(input('Número: '))
while num != 0: #Le a entrada do usuário e escreve numa lista
    num = int(input('Número: '))
    lista.append(f'{num}\n')

arq.writelines(lista) #Escreve a lista no arq
arq.close()
print('fim')