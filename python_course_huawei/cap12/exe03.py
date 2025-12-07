"""
Escreva uma função que receba dois números inteiros A e B como parâmetros de entrada e retorne
True se A for divisível por B e False caso contrário. Escreva o programa principal para testar a função
"""

def a_is_div_by_b(a:int, b:int) -> bool:
    """
    Decide se a é divisível por b
    -> a: int
    -> b: int
    -> return: Retorna True ou False se a%b == 0
    """
    return True if a % b == 0 else False

# entrada dos valores para a função
valor_a = int(input('Número 1:'))
valor_b = int(input('Número 2:'))

# recebe a saída da função e apresenta o resultado de acordo.
if a_is_div_by_b(valor_a, valor_b):
    print('A é divisível por B')
else:
    print('A não é divisível por B')

