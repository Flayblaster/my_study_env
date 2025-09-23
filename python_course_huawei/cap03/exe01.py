"""Escreva um programa que leia os nomes de três pessoas de uma família: mãe, pai e criança. O
programa deve exibir na tela a mensagem.
"Os adultos {mãe} e {pai} são os responsáveis por {criança}"
Faça de dois modos: com o método .format() e com f-string
"""

mom = str(input('Name of mother: '))
dad = str(input('Name of dad: '))
child = str(input('Name of child: '))

print(F'Os adultos {mom} e {dad} são os responsáveis por {child}')
print('Os adultos {0} e {1} são os responsáveis por {2}'.format(mom, dad, child))
