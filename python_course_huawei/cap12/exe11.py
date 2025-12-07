"""
Escreva uma função que carregue e retorne uma lista com todos os elementos da sequência de
Fibonacci menores que um parâmetro passado à função.
Escreva o programa principal para testar a função.
A sequência de Fibonacci é definida da seguinte forma: a) os dois primeiros termos da sequência
são 0 e 1. Do terceiro termo em diante cada termo é a soma dos dois anteriores.
Caso de teste: Se ValorLimite = 120, então a sequência é: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
"""

def fibonacci():
    """
    Somente faz o cálculo de fibonacci.
    -> n1: int, primeiro valor
    -> n2: int, segundo valor
    -> n3: int, terceiro valor
    -> limit: int, limite
    -> c: int, contador
    """
    # declaração de variáveis
    n1 = 0
    n2 = 1
    limit = 120
    c = 0

    print(n1, n2, end=' ')
    # após os primeiros valores serem apresentados
    # começa um looping que n3 é igual a soma dos dois valores anteriores (n1, n2)
    # e antes do próximo looping os valores de n2 e n1 é atualizado, para o cáculo do próximo valor da sequência
    while limit != c:
        n3 = n1 + n2
        print(n3, end=' ')
        n1 = n2
        n2 = n3
        c +=  1

fibonacci()