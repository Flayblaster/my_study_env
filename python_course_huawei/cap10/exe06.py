"""
Escreva um programa que permaneça em laço lendo do teclado números inteiros entre 1 e 9. Outros
valores devem ser ignorados. Esse laço termina quando for digitado zero ou qualquer valor negativo.
O objetivo deste programa é contar quantas vezes cada valor entre 1 e 9 foi digitado.
Ao término do laço de leitura o programa deve mostrar quais valores foram digitados e quantas vezes
cada um. Obrigatoriamente use um dicionário
"""
num = 1
counter = 0

while num >= 1:
    num = int(input('Numero: '))
    if num > 9:
        print('Valor inválido')
        continue
    counter += 1
else:
    counter -= 1
    print('Programa finalizado')

print(f'Quantidade de números que foram digitados: {counter}')