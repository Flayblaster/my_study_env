"""
Altere a solução do ex.resolvido 7.3 para exibir os resultados em ordem inversa à ordem de leitura
Dica: Aplique o metodo .reverse() apresentado no quadro 7.2 e visto no vídeo do exemplo 7.10
"""

qtd = int(input('Quantidade de números: '))
lista = []
try:
    for _ in range(qtd):
        entrada = float(input('Número: '))
        lista.append(entrada)
except ValueError:
    print('Deu erro, escreve certo')

lista.reverse()
for x in lista:
    print(f'{x:.2f}')