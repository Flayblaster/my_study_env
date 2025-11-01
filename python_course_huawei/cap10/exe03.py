"""
Escreva um programa que leia dados dos Estados brasileiros: Sigla, Nome, Capital e PIB. A Sigla deve
ser usada como chave para o dicionário e o valor deve ser uma tupla formada com (Nome, Capital,
PIB). A leitura termina quando um string vazio for fornecido para a Sigla. Exibir os dados na tela
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
    info = (nome, capital, PIB)
    uf[sigla] = info

print(f'    {'Estado':15} {'Capital':15} {'PIB (R$ bi)':>10}')
for sigla, dados in uf.items():
    print(f'({sigla}) - {dados[0]:15} - {dados[1]:15} - {dados[2]:10.1f}')
