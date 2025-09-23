"""Uma empresa comercial trabalha com 3 vendedores externos e os remunera com R$ 1200,00 fixos
mais comissão de 6% sobre o valor total vendido no mês. Escreva um programa que leia o nome e o
total vendido pelos 3 vendedores, calcule e exiba na tela a mensagem de saída conforme o exemplo
a seguir. Exiba os valores numéricos com duas casas decimais.
"""

nome_v1 = str(input('Nome do vendedor: '))
vendas_v1  = float(input(f'Vendas do {nome_v1}: '))

nome_v2 = str(input('Nome do vendedor: '))
vendas_v2 = float(input(f'Vendas do {nome_v2}: '))

nome_v3 = str(input('Nome do vendedor: '))
vendas_v3 = float(input(f'Vendas do {nome_v3}: '))

comissao_v1 = vendas_v1*0.06 + 1200
comissao_v2 = vendas_v2*0.06 + 1200
comissao_v3 = vendas_v3*0.06 + 1200

print(f'Vendedor {nome_v1} vendeu R$ {vendas_v1} e faz jus a uma comissão de R$ {comissao_v1:.2f}')
print(f'Vendedor {nome_v2} vendeu R$ {vendas_v2} e faz jus a uma comissão de R$ {comissao_v2:.2f}')
print(f'Vendedor {nome_v3} vendeu R$ {vendas_v3} e faz jus a uma comissão de R$ {comissao_v3:.2f}')