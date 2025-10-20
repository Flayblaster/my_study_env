"""
Escreva um programa que permaneça em laço lendo três dados de um produto: o código (int), o
preço de compra (float) e o preço de venda(float). Com esses dados forme uma tupla e armazene-a
em uma lista. Os três dados devem ser lidos em uma única linha separados por espaço em branco.
O laço termina quando forem digitados três zeros: 0 0 0
Em seguida, para todas as tuplas presentes na lista, exiba o código do produto e a margem bruta de
lucro do produto em porcentagem e com uma casa decimal.
A margem bruta de lucro é calculada com a expressão:
𝑀𝑎𝑟𝑔𝑒𝑚𝐵𝑟𝑢𝑡𝑎 = ((𝑃𝑟𝑒ç𝑜 𝑉𝑒𝑛𝑑𝑎/𝑃𝑟𝑒ç𝑜 𝑑𝑒 𝐶𝑜𝑚𝑝𝑡𝑎) − 1 ) . 100%
"""
lista_produtos = []

while True:
    produto = (int(input('Código do produto: ')), float(input('Preço de Compra: ')), float(input('Preço de Venda: ')))

    if 0 == produto[0] and 0 == produto[1] and 0 == produto[0]:
        print('FIM')
        break
    else:
        lista_produtos.append(produto)

for prodt in lista_produtos:
    margem_bruta = ((prodt[2]/prodt[1]) - 1) * 100
    print(f'Código do produto: {prodt[0]}')
    print(f'Margem Bruta: %{margem_bruta:.1f}')
    print('------------------------------------')