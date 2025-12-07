"""
Escreva uma função que receba como parâmetro de entrada um número inteiro de 5 dígitos de
[10000, 99999] que represente códigos de produtos vendidos em uma loja. A função deve calcular e
retornar o dígito verificador utilizando a regra de cálculo explicada a seguir. Escreva o programa
principal para testar a função.
Regra: Considere o código 31483, em que cada dígito é multiplicado por um peso começando em 2 e
terminando em 6. Os valores obtidos são somados, e do total obtido calcula-se o resto de sua
divisão por 7.
"""

def verif_digit(cod:str) -> int:
    """
    Calcula o digito verificador conforme fórmula e código do produto.
    -> fórmula: cada digito multiplicado por 2, depois de somado os valores,
    calcula-se o resto da divisão por 7.
    -> cod: str, código do produto
    -> soma: soma os dígitos do código
    -> peso: multiplica os dígitos do código
    -> resto: recebe o resto da divisão por 7, valor final
    -> return: int, retorna o digito verificador
    """
    soma = 0
    peso = 2
    for item in cod:
        soma += int(item)*peso
        peso += 1
    resto = soma%7
    return resto

codigo = str(input('Código do produto: '))
print(f'Digito verificador: {verif_digit(codigo)}')