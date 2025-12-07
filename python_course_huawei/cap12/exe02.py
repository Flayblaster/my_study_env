"""
Escreva uma função que recebe um número inteiro como parâmetro de entrada e retorna o texto
"PAR" ou "ÍMPAR". Use-a em um programa principal
"""

def par_impar(num: int) -> str:
    """
    Decide se num é impar ou par
    -> num: int
    -> return: Retorna uma str, 'par' ou 'ímpar'
    """
    if num % 2 == 0:
        return "PAR"
    else:
        return "ÍMPAR"

# lê a entrada, chama a função e apresenta para o usuário
print(par_impar(int(input('Número: '))))

