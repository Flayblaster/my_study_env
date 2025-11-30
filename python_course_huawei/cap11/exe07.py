"""
Escreva um programa que grave as duas linhas de texto abaixo em um arquivo. Em seguida leia esse
arquivo e mostre na tela o que foi lido. As codificações que vamos testar são ANSI e UTF-8 e elas
deverão ser lidas do teclado.
"""
cod_gravacao = input('Codificação de Gravação: ')
cod_leitura = input('Codificação de Leitura: ')

arq = open('arq_exe07_cap11.txt', 'w', enconding=cod_gravacao)

