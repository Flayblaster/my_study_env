"""
Escreva uma função que receba como parâmetro de entrada dois números reais Min e Max. Essa
função deve ler do teclado um número real e retorná-lo caso esteja dentro do intervalo fechado
[Min, Max]. Caso contrário, a função deve exibir uma mensagem de erro e ler um novo valor.
"""

def is_in_interval(minl:int, maxl:int) -> tuple:
    """
    Lê dois valores, minl e maxl, e uma entrada do usuário, a, depois decide se está dentro do invalor de minl e maxl.
    -> a: float, entrada do usuário
    -> minl: valor minímo
    -> maxl: valor máximo
    -> return: tuple, com o valor lido e uma str
    """
    a = float(input('Valor: '))
    while maxl < a > minl:
        print('Valor fora do intervalo')
        a = float(input('Digite novamente: '))
    else:
        return a, "Valor dentro do intervalo"

# lê os limites decididos pelo usuário
min_ = int(input('Valor minímo: '))
max_ = int(input('Valor máximo: '))

# valor recebe o retorno da função
valor = is_in_interval(min_, max_)
# apresenta para o usuário
print(f'{valor[0]} - {valor[1]} de {min_} até {max_}')