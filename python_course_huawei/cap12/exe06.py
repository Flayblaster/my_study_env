"""
Escreva um programa que leia quatro notas de um aluno, calcule a média e mostre a situação do
aluno que será 'APROVADO' ou 'REPROVADO'.
O programa deve ler as quatro notas separadas por um espaço em branco em uma mesma linha de
digitação. As notas lidas devem ser separadas, convertidas para número real e inseridas em uma
lista, junto com a média e a situação do aluno. Isso tudo deverá ser feito dentro de uma função.
Médias a partir de 7.0 indicam aprovação; menos que isso reprovação.
A ordem das notas na digitação deve ser: P1 P2 P3 NT
Escreva o programa principal para testar sua função. A saída deste programa deve mostrar todas as
notas, a média e a situação (você é livre para elaborar o layout de saída).
Cálculo Média MF = 0.3 * P1 + 0.3 * P2 + 0.3 * P3 + 0.1 * NT
"""

def media_calc(*notas) -> str:
    """
    Recebe uma tupla com as notas de um aluno, fazendo o cálculo da média com pesos do aluno.
    -> media: float
    -> notas: tuplas, recebe as notas
    -> return: Retorna uma str conforme resultado da média
    """
    media = 0.3*notas[0] + 0.3*notas[1] + 0.3*notas[2] +  0.1*notas[3]
    return f'Aprovado!! A média do aluno foi: {media:.2f}' if media >= 6.0 \
        else f'Reprovado!! A média do aluno foi: {media:.2f}'

# lê todas as notas do aluno
nota1 = float(input('1º Nota: '))
nota2 = float(input('2º Nota: '))
nota3 = float(input('3º Nota: '))
nota4 = float(input('4º Nota: '))

# chama a função e apresenta o resultado ao usuário
print(media_calc(nota1, nota2, nota3, nota4))
