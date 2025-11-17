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
maiúsculas com o método .upper().
Para cada veículo leia todos os dados e carregue em um dicionário. Se uma placa já existente for
digitada o programa deve avisar que já existe, mostrar seus dados e se usuário quiser fazer alteração
em algum dado basta digitar o novo valor. Para os campos em que nada for digitado deve ser mantido
o valor já cadastrado.
Ao final do laço mostre os dados na tela com uma formatação legível.
Desafio Inclua no programa uma validação da placa, seguindo as seguintes regras:
a) Deve ter 7 caracteres
b) Os três primeiros devem ser letras
c) Os caracteres 4, 6 e 7 devem ser algarismos
d) O caractere 5 pode ser número (placa antiga) ou letra (nova placa padrão Mercosul)
"""
carro = dict()
alfabeto = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',)

def verif_placa():
    while True:
        x = str(input('Placa: ')).upper()
        if 'FIM' in x:
            return x
        elif not 7 == len(x):
            print('Tamanho incorreto')
        elif not x[0:3].isalpha():
            print('Formato incorreto, os caracteres 1, 2 e 3 devem ser alfabéticos')
        elif not ((x[3].isdigit()) and (x[5].isdigit()) and (x[6].isdigit())):
            print('Formato incorreto, os caracteres 4, 6 e 7 devem ser numéricos')
        else:
            break
    return x

while True:
    placa = verif_placa()
    if 'FIM' in placa:
        print('Programa Finalizado')
    if placa in carro:
        print('Essa placa já existe')
        pergt1 = str(input('Deseja alterar algum valor? ')).lower()
        if 's' in pergt1:
            print(f'Placa: {placa} - Marca: {carro[placa][0]} - Modelo: {carro[placa][1]} - Tipo: {carro[placa][2]} - Kilometragem: {carro[placa][3]} - Data de Compra: {carro[placa][4]}')
            pergt2 = str(input('Qual dado: ')).lower()
            if 'marca' in pergt2:
                carro[placa][0] = str(input('Marca: '))
            elif 'modelo' in pergt2:
                carro[placa][1] = str(input('Modelo: '))
            elif 'tipo' in pergt2:
                carro[placa][2] = str(input('Tipo: '))
            elif 'kilo' in pergt2:
                carro[placa][3] = str(input('Kilometragem: '))
            elif 'data' in pergt2:
                carro[placa][4] = str(input('Data da Compra: '))
            print('Valor alterado')
            continue
        else:
            placa = verif_placa()
    marca = str(input('Marca: '))
    modelo = str(input('Modelo: '))
    tipo = str(input('Tipo: '))
    kilometragem = str(input('Kilometragem: '))
    data_compra = str(input('Data da Compra: '))
    carro[placa] = [marca, modelo, tipo, kilometragem, data_compra]


for placa, info in carro.items():
    print(placa, info)