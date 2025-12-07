"""
Escreva uma função que receba uma lista como parâmetro de entrada e retorne uma tupla contendo
quatro valores na seguinte ordem: a soma, a média, o menor e o maior valor dentre todos os
elementos nela contidos. Considere que nessa lista ocorram apenas números reais. Escreva um
programa para testar essa função, exibindo na tela os resultados.
"""

def smmm(valores: list) -> tuple:
    """
    Soma, média, maior e menor, recebe uma lista de valores e realiza todos esses cáculos
    -> return: tuple, retorna o resultado
    """
    soma = sum(valores)
    media = soma/len(valores)
    maior = max(valores)
    menor = min(valores)
    return soma, media, maior, menor


lista = list()

# para cada item lido é posto numa lista, assim ela como parâmetro, chamando a função
qtde = int(input('Quantidade de valores: '))
for _ in range(qtde):
    num = int(input('Valor: '))
    lista.append(num)
res = smmm(lista)

# apresenta o resultado ao usuário
print(f'A soma é {res[0]}, a média é {res[1]:.2f}, o maior é {res[2]}, o menor é {res[3]}')