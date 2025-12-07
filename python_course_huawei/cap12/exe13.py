"""
Escreva uma função que receba uma lista de números inteiros e elimine os eventuais elementos
repetidos nela contidos e a retorne.
Dica: Dentro da função use a classe set.
Escreva o programa principal para testar a função.
"""
def no_repeat(*nums_:list) -> set:
    """
    Uma função que remove valores repetidos, usando a classe set
    -> nums: list, recebe todos os valores do usuário
    -> nr: set
    -> return: set, retorna o set
    """
    nr = set()
    # para cada item em nums, adicione ao conjunto nr
    for item in nums_:
        nr.update(item)
    return nr

nums = list()
# lê a entrada do usuário e adiciona os valores a lista nums
qtde = int(input('Quantidade de números: '))
for _ in range(qtde):
    nums.append(int(input('Numero: ')))

# apresenta o resultado ao usuário
print(no_repeat(nums))