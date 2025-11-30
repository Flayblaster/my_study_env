"""
Escreva um programa para registrar os seguintes dados de uma frota de veículos de uma empresa:
Placa (string – chave – obrigatório todas as letras maiúsculas)
Marca
Modelo
Tipo (caminhão, furgão, automóvel, motocicleta, etc)
Kilometragem
Data da Compra (string no formato AAAAMMDD – ano,mês,dia)
O programa deve ficar em laço enquanto a Placa for digitada. O laço termina quando for digitado FIM
para a placa. Se for digitada uma placa com letras minúsculas o programa deve convertê-las para
maiúsculas com o mélodo .upper().
Para cada veículo leia todos os dados e carregue em um dicionário. Se uma placa já existente for
digitada o programa deve avisar que já existe, mostrar seus dados e se usuário quiser fazer alteração
em algum dado basta digitar o novo valor. Para os campos em que nada for digitado deve ser mantido
o valor já cadastrado.
Ao final do laço grave todos os dados em um arquivo CSV usando o caractere ";" como delimitador
"""

import random

# declaração de variáveis
veiculos = dict()
alf = ('a','b','c','d','e','f','g','h','i','j','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
tipo_ = ('caminhão', 'furgão', 'motocicleta', 'hatch', 'cupê', 'perua', 'cross', 'suv')
marca_ = ('Volksvagen', 'Chevrolet', 'BMW', 'Mercedes', 'Toyota', 'AMG', 'Honda', 'Ford', 'Fiat', 'Jeep', 'Kia')
date_ = ('10/02/2000', '01/11/1972', '26/06/2023', '18/09/2015', '19/12/2014', '02/05/2005', '21/10/2025')
c = 0

# Gera placas prontas
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

# gera as iformações necesárias para o veiculo
qtd_placas = int(input('Quantidade de placas: '))
while c != qtd_placas:
    placa = verif_placa()
    marca = marca_[random.randint(0, 10)]
    tipo = tipo_[random.randint(0, 7)]
    kilometragem = f'{random.randint(0, 400000)}'
    date_acquisition = date_[random.randint(0, 6)]
    info = (marca, tipo, kilometragem, date_acquisition)
    veiculos[placa] = info
    c += 1

# mostra as informações na tela de formar tabelar
print(f'{'PLACA':<10} {"MARCA":<14} {"TIPO":<15} {"KILOMETRAGEM":<15} {"DATA DE COMPRA"}')
for placa, info in veiculos.items():
    print(f'{placa.upper():10} {info[0].upper():14} {info[1].title():15} {int(info[2]):<15.2f} {info[3]:8}')