"""
Escreva um programa que permaneça em laço lendo quantidades (números inteiros) de produtos
vendidos. O laço termina quando for digitado zero ou um valor negativo. Ao término do laço exiba na
tela a soma de todas as quantidades digitadas (se for digitado um negativo para sair do laço ele não
deve afetar o total).
"""
soma = 0
while True:
    num = int(input('Número: '))
    if num > 0:
        soma += num
    else:
        print('Fim do programa')
        break
print(f'A soma de todos os valores é: {soma}')