"""
Crie uma função que receba um ângulo em graus, e retorne esse ângulo convertido para radianos. O
valor de PI está disponível no módulo math. Importe o módulo e use math.pi
Escreva o programa principal para testar a função.
Regra AngRadiano = AngGraus * PI / 180
"""

from math import pi

def convert_radian(ang_graus:float) -> float:
    """
    Converte um ângulo em graus para radianos
    -> ang_graus: float, ângulo em graus
    -> ang_radian: float, ângulo em radianos
    -> return: float, retorna o resultado
    """
    ang_radian = ang_graus*pi/180
    return ang_radian

# recebe o valor do angulo a ser convertido
ang = float(input('Ângulo em graus: '))
# chama a função e apresenta para o usuário
angulo_convertido = convert_radian(ang)
print(f'{ang} em Radiano é: {angulo_convertido:.2f}')
