"""
Em um determinado momento do dia a cotação de compra das moedas estrangeiras é a seguinte:
Dólar: US$ 1.00 = R$ 4.89 - Euro: € 1.00 = R$ 5.26 - Libra Esterlina: £ 1.00 = R$ 6.17
Escreva um programa que leia o tipo (D, E ou L maiúsculo) e o valor de moeda estrangeira que se
quer comprar e calcule o valor em reais necessários.
"""

moeda = str(input('Moeda requerida: ')).lower()
qtd_estrange = float(input('Valor requisitado da moeda: '))

if moeda in 'e':
    qtd_reais = qtd_estrange*5.26
    print(f'Será necessário R${qtd_reais:.2f}')
elif moeda in 'd':
    qtd_reais = qtd_estrange*4.89
    print(f'Será necessário R${qtd_reais:.2f}')
elif moeda in 'l':
    qtd_reais = qtd_estrange*6.17
    print(f'Será necessário R${qtd_reais:.2f}')
else:
    print('Valor inválido')