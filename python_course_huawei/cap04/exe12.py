"""
Leia um número inteiro entre 1 e 12 e exiba o mês correspondente. Caso seja digitado um número
fora desse intervalo, o programa deve exibir uma mensagem informando que não existe mês com
este número.
"""

meses = ('Janeiro', 'Fevereiro', 'março', 'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

intnum = int(input('Digite um número de 1 a 12: '))
if  1 <= intnum <= 12:
    print(f'Mês correspondente: ({intnum}) - {meses[intnum-1]}')
else:
    print('Valor inválido!!!')
