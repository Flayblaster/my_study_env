"""
Escreva um programa que permaneça em laço lendo cadeias de caracteres (strings). Para cada
cadeia digitada o programa deve exibir a cadeia seguida da quantidade de caracteres que ela
contém. O programa termina quando for digitado "FIM" (em letras maiúsculas).
"""
entrada = str(input('Palavra: '))

while not (entrada in 'FIM'):
    cont = 0
    for i in entrada:
        cont += 1
    print(f'{entrada}, Letras: {cont}')
    entrada = str(input('Palavra: '))

