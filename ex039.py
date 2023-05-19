#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe
# , de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora
# exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.
import datetime
from datetime import date
atual = date.today().year
nascimento = int(input('Digite seu ano de nascimento:'))
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento,(atual - nascimento), atual))
if 2023 - nascimento < 18:
    print('Ainda faltam {} anos para seu alistamento'.format((nascimento+18)- atual))
    print('Seu alistamento será em {}! '.format(nascimento+18))
elif 2023 - nascimento > 18:
    print('Voce já deveria ter se alistado há {} anos'.format(atual - (nascimento+18)))
    print('Seu alistamento foi em {}!'.format(nascimento+18))
else:
    print('Voce tem que se alistar imediatamente!')



