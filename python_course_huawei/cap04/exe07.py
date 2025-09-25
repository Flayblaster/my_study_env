"""Em Albalândia mulheres e homens podem servir o exército do país. O serviço é opcional e é muito
comum que as pessoas se apresentem para o serviço em algum momento da vida. Existe uma única
restrição para ingresso que é a idade da pessoa: para mulheres a idade aceita é entre 21 e 34 anos;
para homens a idade aceita é entre 18 e 39 anos. Escreva um programa que leia três dados de
entrada: nome da pessoa, idade e sexo e informe se a pessoa será aceita ou não para o serviço.
Para o sexo deve ser lido apenas 1 caractere que pode ser 'f' ou 'F' para feminino e 'm' ou 'M'
para masculino, qualquer coisa diferente deve ser informado como inválido."""

nome = str(input('Nome do candidato: '))
idade = int(input('Idade: '))
sexo = str(input('Sexo: ')).lower()

if 'f' in sexo:
    if 21 <= idade <= 34:
        print('Você foi aceita!!')
    else:
        print('Você foi rejeitada!')
elif 'm' in sexo:
    if 18 <= idade <= 39:
        print('Você foi aceito!!')
    else:
        print('Você foi rejeitado!')
else:
    print('sexo inválido')
