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


def betwen(a:int, b:int) -> list:
    """
    Para cada número primo dentro do intervalo de a - b, é criado uma lista com estes.
    -> a: int, limite inicial
    -> b: int, limite final
    -> prim_list: list, recebe os valores primos
    -> return: list, retorna a lista com os valores
    """
    prim_list = list()
    # é iterado todos os valores dentro do intervalo
    # para cada num, é decidido se é primo ou não
    # os primos são adicionados na lista
    for num in range(a, b):
        if is_prime(num):
            prim_list.append(num)
    return prim_list

# lê o intervalo decidido pelo usuário
a = int(input('Número a:'))
b = int(input('Número b:'))
# apresenta o resultado
print(f'Dentro do intevalo de {a} - {b}, temos os seguintes primos:')
for item in betwen(a, b):
    print(item, end=' ')