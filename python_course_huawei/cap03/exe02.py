"""Escreva um programa que leia um texto e mostre na tela o texto e a quantidade de caracteres que
ele contém, usando a seguinte mensagem:
O texto {AquiColoqueOTexto} contém {Quantidade} caracteres
Faça de dois modos: com o.format() e com f-string"""

text = str(input('Escreva uma frase: '))

text = text.strip()
letter_count = len(text)
print(f'O texto "{text}" contém {letter_count} caracteres')
