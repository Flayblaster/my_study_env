"""
Escreva um programa que permaneça em laço de modo que em cada repetição seja lido e
armazenado em uma lista o nome de uma pessoa. O laço termina quando o usuário entrar com um
string vazio.
Exiba na tela a lista de nomes em ordem alfabética e precedida de um número de ordem começando
em 1.
"""
lista = []
c = 0
while True:
    nome = str(input('Primeiro nome: ')).title().strip()
    sobrenome = str(input('Sobrenome: ')).title().strip()
    usuario = nome+' '+sobrenome
    if nome in '':
        print('Fim')
        break
    else:
        lista.append(usuario)
        lista.sort()
for user in lista:
    c += 1
    print(f'{c}. {user}')