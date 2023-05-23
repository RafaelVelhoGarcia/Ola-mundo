#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
from datetime import date
nascimento = int(input('Ano de nascimento:'))
idade = date.today().year - nascimento
print('O atleta tem {} anos'.format(idade))
if    0 < idade <= 9:
    print('Classificaçao: mirim')
elif idade <= 14:
    print('Classificaçao: infantil')
elif idade <= 19:
    print('Classificaçao : Junior')
elif idade <= 25:
    print('Classificaçao : Senior')
else:
    print('Classificaçao : MASTER')


