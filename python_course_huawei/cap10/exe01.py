"""
Escreva um programa que leia do teclado o código de um produto e seu preço unitário. O código é
um string e o preço é real. Acrescente o par código:preço em um dicionário. O programa deve
verificar se o código já está no dicionário e neste caso deve emitir uma mensagem de erro. O laço
termina quando for fornecido um string vazio para o código. Ao final, exibir código e preço, um
produto em cada linha.
"""
par = {}
preco = 0

codigo = str(input('Código: '))
while codigo != '':
    if codigo in par:
        print('Produto já existe')
        continue
    else:
        preco = float(input('Preço: '))
        par[codigo] = preco
    codigo = str(input('Código: '))
else:
    print('Programa Finalizado')

print('Preço dos prudutos')
for cod, preco in par.items():
    print(f'    Produto {cod} custa R$ {preco}')


