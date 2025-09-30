"""
Reescreva o Exercício Resolvido 5.5 de modo a eliminar o comando if que foi acrescentado dentro
do laço while. Procure pensar em uma forma de eliminar esse condicional e ao mesmo tempo
manter o programa correto, totalizando e contando os valores diferentes de zero que forem
digitados.
Dica: .
"""

soma = 0
qtde = -1
num = 1

while num != 0:
    num = int(input('Digite um número: '))
    soma += num
    qtde += 1

print(f'Soma: {soma}')
print(f'Quantidade de valores: {qtde}')