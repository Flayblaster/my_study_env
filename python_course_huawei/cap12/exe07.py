"""
Escreva um programa que verifique se um número inteiro lido é primo. Lembrando: um número
primo é divisível apenas por 1 e por ele mesmo. A verificação do primo deve ser feita dentro de uma
função.
"""

def is_prime(num_:int) -> bool:
    """
    Lê um número e decide se é primo, atráves de vários testes.
    -> num_:int
    -> return: bool, retorna True para primo e False para não primo
    """
    # se igual a 1, 2 primo. Divisível por 2 não primo
    if num_ == 1:
        return False
    elif num_ == 2:
        return True
    elif num_ % 2 == 0:
        return False
    else:
        # se num_ é divisível por i = 3: Não primo
        # caso contrário, a cada looping, i += 2
        # até i chegar ao valor da raiz, logo, esse valor não possuí divisores, então Primo
        raiz = pow(num_, 0.5)
        i = 3
        while i <= raiz:
            if num_ % i == 0:
                return False
            i += 2
        return True

# entrada do usuário para a função
num = int(input("Numero: "))
# apresentação do resultado
if is_prime(num):
    print(f'{num} é primo')
else:
    print(f'{num} não é primo')



