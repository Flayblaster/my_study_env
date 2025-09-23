"""Escreva um programa que leia três números reais em objetos denominados A, B e C. O programa
deve calcular e mostrar na tela os resultados das fórmulas a seguir, usando 3 casas decimais."""

A = float(input('Número A: '))
B = float(input('Número B: '))
C = float(input('Número C: '))

R1 = A + B + C
R2 = A*B*C
R3 = 2*(A+B) - C
R4 = (A+B+C)/3
R5 = (2*B + 3*C)/5*A
R6 = A**2 + B**2

print(F'{R1:.3f}\n'
      F'{R2:.3f}\n'
      F'{R3:.3f}\n'
      F'{R4:.3f}\n'
      F'{R5:.3f}\n'
      F'{R6:.3f}')