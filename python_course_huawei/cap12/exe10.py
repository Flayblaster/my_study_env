"""
Crie uma função que receba um número de 1 a 12 e retorne nome do mês correspondente. Se o valor
for outro o retorno da função deve ser o string "Inválido".
Escreva o programa principal para testar a função.
"""

def month(n_:int) -> str:
    """
    Retorna o mês, por escrito, correspondente ao número recebido
    -> lista_meses: list, abre uma lista com os meses por escrito
    -> return: str, retorna o mês correspondente
    """
    lista_meses = ['janeiro', 'fevereiro', 'março',
                   'abril', 'maio', 'junho',
                   'julho', 'agosto', 'setembro',
                   'novembro', 'outubro', 'dezembro']
    return lista_meses[n_].title()

# lê a entrada, chama a função e apresenta para o usuário
n = int(input('Mês: '))
print(f'O mês correspondente ao número {n} é {month(n-1)}')