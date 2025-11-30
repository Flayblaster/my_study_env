"""
Escreva um programa que leia um número inteiro N (10 < N < 10.000) e grave um arquivo com N linhas
com os dados listados na tabela abaixo. O arquivo deve ter o nome 'Estoque.csv e deve usar o
caractere ';' (ponto e vírgula) como delimitador. Não é necessário que o arquivo esteja ordenado.
"""
import random

estoque = dict()
arq = open('arq_exe10_cap11.csv', 'w')

N = 0

num_linhas = int(input('Número de Linhas: '))
while N != num_linhas:
    codigo = random.randint(10000, 50000)
    while codigo in estoque:
        codigo = random.randint(10000, 50000)
    qtd_est = random.randint(1, 3801)
    preco_unid = random.random()*1000
    while not 435.9 > preco_unid > 1.8:
        preco_unid = random.random() * 1000
    icms = str(input('Alíquota do ICMS: '))
    while not icms in ('7', '12', '18'):
        icms = str(input('Alíquota do ICMS: '))
    else:
        print('valor correto')
    N += 1
    estoque[f'{codigo}'] = f'{qtd_est};{preco_unid:.2f};{icms}'

for item in estoque.items():
    arq.writelines(item)
print(estoque)
