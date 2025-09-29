"""
No comércio, o conceito de Margem Bruta é uma porcentagem aplicada ao preço de custo
para se obter o preço de venda. Uma loja tem como política comercial aplicar uma margem bruta de
45% quando o preço de custo de um produto é menor ou igual a R$100,00. Se o produto custa mais
que isso a margem bruta é de 35%. Escreva um programa que leia o preço de custo do produto e
mostre na tela qual o seu preço de venda, com duas casas decimais.
"""

custo = float(input('Custo do produto: '))
margem_bruta_maior = 0.45
margem_bruta_menor = 0.35
if custo >= 100:
    custo_venda = (custo * margem_bruta_maior) + custo
else:
    custo_venda = (custo * margem_bruta_menor) + custo

print(f'O custo de venda do produto é de {custo_venda}')