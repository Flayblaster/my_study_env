"""
Escreva uma função que receba um parâmetro string. Essa função deve retornar True se o string for
palíndromo e False caso não seja. Espaços em branco, algarismos e sinais de pontuação devem ser
eliminados, se estiverem presentes no parâmetro.
Definição Um string palíndromo é aquele que pode ser lido da esquerda para a direita e da direita para a
esquerda, por exemplo: IRENE RI -> elimine o espaço em branco IRENERI
Outros SUBI NO ONIBUS
palíndromos ANOTARAM A DATA DA MARATONA
para teste A CARA RAJADA DA JARARACA
AABBCCDDCCBBAA (não é uma frase, mas é palíndromo)
"""

def is_palindromo(frase:str) -> bool:
    frase = frase.lower().replace(' ', '')
    tamanho = len(frase)
    if tamanho % 2 == 0:
        tamanho = int(tamanho/2)
        metade1 = frase[0:tamanho]
        metade2 = frase[tamanho:][::-1]
    else:
        tamanho = int(tamanho/2)
        metade1 = frase[0:tamanho]
        metade2 = frase[tamanho+1:][::-1]
    return True if metade2 == metade1 else False

print(is_palindromo('anotaram a data da maratona'))

