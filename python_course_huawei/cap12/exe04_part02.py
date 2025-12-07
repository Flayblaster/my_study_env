"""
No exercício resolvido 12.4 não foi feita uma validação do código lido do teclado. Sendo assim,
experimente digitar códigos que são menores que 10000 ou maiores que 99999 e veja o que
acontece.
Em seguida implemente a validação do código lido e só efetue o cálculo do dígito verificador se ele
for válido.
"""

def verif_digit(cod:str) -> int:
    """
    Calcula o digito verificador conforme fórmula e código do produto.
    Também faz a verificação do tamanho do código, sendo ele de 5 dígitos.
    -> fórmula: cada digito multiplicado por 2, após somado os valores,
    calcula-se o resto da divisão por 7.
    -> cod: str, código do produto
    -> soma: soma os dígitos do código
    -> peso: multiplica os dígitos do código
    -> resto: recebe o resto da divisão por 7, valor final
    -> return: int, retorna o digito verificador
    """
    soma = 0
    peso = 2
    while len(cod) != 5:
        cod = str(input('Digite o código novamente: '))
    for item in cod:
        soma += int(item)*peso
        peso += 1
    resto = soma%7
    return resto

# lê a entrada do usuário
codigo = str(input('Código do produto: '))
# apresenta e chama a função
print(f'Digito verificador: {verif_digit(codigo)}')