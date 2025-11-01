"""
Escreva um programa que leia dados dos Estados brasileiros: Sigla, Nome, Capital e PIB. A Sigla deve
ser usada como chave para o dicionário e o valor deve ser um dicionário aninhado contendo os
objetos Nome, Capital e PIB. Um string vazio para a Sigla termina a leitura. Exibir os dados na tela.
"""
uf = {}


while True:
    sigla = str(input('Sigla: ')).upper()
    if sigla == '':
        break
    elif sigla in uf:
        while sigla in uf:
            print('Esse estado já foi cadastrado!!!')
            sigla = str(input('Sigla: ')).upper()
        else:
            print('Sigla cadastrada')
    nome = str(input('Nome: ')).title()
    capital = str(input('Capital: ')).title()
    PIB = float(input('PIB: '))
    info = {'nome': nome, 'capital': capital, 'pib': PIB}
    uf[sigla] = info


print(f'    {'Estado':15} {'Capital':15} {'PIB (R$ bi)':>10}')
for sigla, dados in uf.items():
    print(f'({sigla}) - {dados['nome']:15} - {dados['capital']:15} - {dados['pib']:10.1f}')
