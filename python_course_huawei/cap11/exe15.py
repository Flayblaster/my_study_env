"""
Escreva um programa para ler o arquivo CSV gerado no exercício proposto 11.7 com os dados de
uma frota de veículos de uma empresa:
Placa (string - chave)
Marca
Modelo
Tipo (caminhão, furgão, automóvel, motocicleta, etc)
Kilometragem
Data da Compra (string no formato AAAAMMDD – ano,mês,dia)
O programa deve ler o arquivo, carregar um dicionário e exibir os dados na tela com um layout legível
"""
import random

# declaração de variáveis
veiculos = dict()
alf = ('a','b','c','d','e','f','g','h','i','j','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
tipo_ = ('caminhão', 'furgão', 'motocicleta', 'hatch', 'cupê', 'perua', 'cross', 'suv')
marca_ = ('Volksvagen', 'Chevrolet', 'BMW', 'Mercedes', 'Toyota', 'AMG', 'Honda', 'Ford', 'Fiat', 'Jeep', 'Kia')
date_ = ('10/02/2000', '01/11/1972', '26/06/2023', '18/09/2015', '19/12/2014', '02/05/2005', '21/10/2025')
c = 0
qtd_placas = int(input('Quantidade de placas: '))

def verif_placa() -> str:
    pos_1 = random.randint(0, 26)
    pos_2 = random.randint(0, 26)
    pos_3 = random.randint(0, 26)
    num_1 = random.randint(0, 9)
    num_2 = random.randint(0, 9)
    num_3 = random.randint(0, 9)
    num_4 = random.randint(0, 9)
    x = alf[pos_1] + alf[pos_2] + alf[pos_3] + f'{num_1}' + f'{num_2}' + f'{num_3}' + f'{num_4}'
    return x

while c != qtd_placas:
    placa = verif_placa()
    if placa in "0":
        break
    marca = marca_[random.randint(0, 10)]
    tipo = tipo_[random.randint(0, 7)]
    kilometragem = f'{random.randint(0, 400000)}'
    date_acquisition = date_[random.randint(0, 6)]
    info = (marca, tipo, kilometragem, date_acquisition)
    veiculos[placa] = info
    c += 1

print(f'{'PLACA':<10} {"MARCA":<14} {"TIPO":<15} {"KILOMETRAGEM":<15} {"DATA DE COMPRA"}')
for placa, info in veiculos.items():
    print(f'{placa.upper():10} {info[0].upper():14} {info[1].title():15} {int(info[2]):<15.2f} {info[3]:8}')