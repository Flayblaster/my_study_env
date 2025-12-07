"""
No exercício resolvido 12.2 foi usado o comando condicional clássico. Altere o código dentro da
função substituindo o if-else clássico por um if de única linha.
"""

# versão simplificada do exercício anterior
def par_impar(num: int) -> str:
    """
    Decide se num é ímpar ou par
    -> num: int
    -> return: retorna a str: 'par' ou 'ímpar'
    """
    return "PAR" if num % 2 == 0 else "ÍMPAR"

# lê a entrada, chama a função e apresenta para o usuário
print(par_impar(int(input('Número: '))))
