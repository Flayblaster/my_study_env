"""
Escreva um programa que leia um número inteiro e informe se esse número é primo ou não.
Lembrando: um número primo é divisível apenas por 1 e por ele mesmo.
"""
while True:
    n = int(input('número: '))
    if n == 0:
        print('Fim do programa')
        break
    elif n != 0:
        cont = 0
        for x in range(1, n+1):
            if n%x == 0:
                cont += 1
        if cont == 2:
            print('Esse número é primo')
        else:
            print('Esse número não é primo')