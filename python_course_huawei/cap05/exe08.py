"""
Uma indústria metalúrgica adota um código de produto com o seguinte formato TMMM, onde T indica
o uso do produto, sendo 1 para residencial; 2 para industrial e MMM indica qual é o produto.
Escreva um programa que permaneça em laço até que seja digitado 0. Em cada repetição leia duas
informações:
a) O código do produto;
b) A quantidade vendida desse produto
O programa deve totalizar separadamente e exibir na tela as quantidades de produtos residenciais e
industriais vendidos. Se o dígito T do código não for 1 ou 2 deve ser mostrado "Tipo Inválido" e a
quantidade deve ser ignorada.
"""
soma_r = soma_i = 0

while True:
    codigo = str(input('Código do produto: '))
    qtde_vendas = int(input('Quantidade vendida: '))
    if codigo == '0':
        print('Programa encerrado')
        break
    elif codigo[0] in '1':
        print('Residencial')
        soma_r += qtde_vendas
    elif codigo[0] in '2':
        print('Industrial')
        soma_i += qtde_vendas
    else:
        print('Código inválido!!!')
print(f'A soma das vendas dos produtos residenciais é: {soma_r}')
print(f'A soma das vendas dos produtos industriais é: {soma_i}')