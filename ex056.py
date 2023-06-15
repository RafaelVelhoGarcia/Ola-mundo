MaiorIdade = 0
MenorIdade = 0
soma = 0
ContF = 0
for c in range(1,5):
    print('{} {}º pessoa {}'.format( '=-'*5,c,'=-'*5))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = input('SEXO [M/F]').strip()
    soma += idade
    if c == 1:
        MaiorIdade = idade
        MaisVelho  = nome
    else:
        if idade > MaiorIdade and sexo in 'Mn':
            MaiorIdade = idade
            MaisVelho = nome
    if idade < 20 and sexo in 'Ff':
        ContF += 1

media = soma / 4
print('A média de idade do grupo é de {:.2f}'.format(media))
print('O homen mais velho tem {} e se chama {}'.format(MaiorIdade,MaisVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(ContF))
