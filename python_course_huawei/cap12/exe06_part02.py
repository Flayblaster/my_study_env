"""
Altere o programa anterior mudando a regra de cálculo da média final. Na nova regra as notas de
prova P1, P2 e P3 devem ser analisadas e a menor nota deve ser descartada. As duas melhores notas
serão chamadas de N1 e N2. A nota de trabalho será considerada e a nova fórmula é:
MF = 0.4 * N1 + 0.4 * N2 + 0.2 * NT
"""

def media_calc(*notas: float) -> str:
    """
    Recebe uma tupla com as notas de um aluno, fazendo o cálculo da média com pesos diferentes para cada nota.
    -> noas: list, somente para facilitar o tratamento das notas
    -> media: float
    -> notas: tuplas, recebe as notas
    -> return: Retorna uma str conforme resultado da média
    """
    noas = list(notas)
    noas.remove(min(notas[0:3])) # remove a menor nota
    media = 0.4*noas[0] + 0.4*noas[1] + 0.2*noas[2]
    return f'Aprovado!! A média do aluno foi: {media:.2f}' if media >= 6.0 \
        else f'Reprovado!! A média do aluno foi: {media:.2f}'

# lê as notas do aluno
nota1 = float(input('1º Nota: '))
nota2 = float(input('2º Nota: '))
nota3 = float(input('3º Nota: '))
nota4 = float(input('4º Nota: '))

# chama a função e apresenta o resultado
print(media_calc(nota1, nota2, nota3, nota4))