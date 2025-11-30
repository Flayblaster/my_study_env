"""
Escreva um programa que grave o arquivo NUMEROS.TXT com 2.000 números, um em cada linha,
gerados com a função randint() do módulo random no intervalo [1, 5.000].
Variação: Altere este programa substituindo o tamanho fixo de 2.000 por uma quantidade de entrada a ser lida
do teclado.
"""
# bibliotecas
import random

# declaração de variáveis
arq = open('numeros.txt', 'w')

# iteração que gera números aleatórios de 1 a 5000 em cada linha do arq
qtde_linhas = int(input('Quantidade de linhas: '))
for _ in range(2000):
    arq.write(f'{random.randint(1, 5000)}\n')

arq.close()
