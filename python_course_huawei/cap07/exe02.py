"""
Altere a solução do ex.resolvido 7.3 incluindo o comando try-except na leitura dos números reais
para evitar a digitação incorreta dos valores. Quando ocorrer uma exceção uma mensagem deve ser
exibida na tela informando esta condição.
Dica: Relembre o tratamento de exceções consultando o capítulo 6, em especial o exemplo 6.4
"""

qtd = int(input('Quantidade de números: '))
lista = []
try:
    for _ in range(qtd):
        entrada = float(input('Número: '))
        lista.append(entrada)
except ValueError:
    print('Deu erro, escreve certo')

for x in lista:
    print(f'{x}:.2f')
