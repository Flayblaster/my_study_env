"""
Nas eleições municipais os municípios com 200 mil eleitores ou mais tem segundo turno caso o
primeiro colocado não tenha mais do que 50% dos votos. Escreva um programa que leia o nome do
município, a quantidade de eleitores e a quantidade de votos do candidato mais votado e informe se
haverá segundo turno ou não.
"""

muni = str(input('Município: '))
qtd_votos = int(input('Quantidade de votos do candidato mais votado: '))
qtd_eleitores = int(input('Quantidade de eleitores: '))

if qtd_eleitores >= 200000:
    second = (100*qtd_votos) / qtd_eleitores
    if second <= 50:
        print('Há de ter segundo turno')
    else:
        print('Não ira ter segundo turno')
else:
    print('Não haverá segundo turno: ')

