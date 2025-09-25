"""Escreva um programa para uma fábrica de calçados que leia o código LL de um calçado, que é um
número inteiro com 2 dígitos. Exiba na tela a linha do calçado, conforme a tabela a seguir. Se o
número fornecido não estiver na tabela, deve-se exibir a mensagem 'Código inválido'"""

ll = int(input('Tamanho do calçado: '))

tamanhos = {16: 'Bebê', 23: 'Infantil Feminino', 25: 'Infantil Masculino',
            29: 'Infantil Esportivo', 42: 'Masculino Formal',
            43: 'Masculino Casual', 49: 'Masculino Esportivo',
            52: 'Feminino Formal Salto Baixo', 53: 'Feminino Formal Salto Alto',
            55: 'Feminino Casual Salto Baixo', 56: 'Feminino Casual Salto Alto',
            59: 'Feminino Esportivo'}

if ll in tamanhos.keys():
    print(f'Linha do calçado: {tamanhos.get(ll)}')
else:
    print('Código inválido')