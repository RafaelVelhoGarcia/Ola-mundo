#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
computador = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente advinhar')
print('-=-' * 20)
jogador = int(input('Em que número estou pensando?'))

if computador == jogador:
    print('Parábens! Voce conseguiu me vencer!')
else :
    print('Ganhei! eu pensei no número {} e não no número {}'.format(computador,jogador))

