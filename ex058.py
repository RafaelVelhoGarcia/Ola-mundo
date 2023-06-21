
from random import randint
print('Sou seu computador...')
print('acabei de pensar entre um número entre 0 e 10')
print('Será que voce conseguiu advinhar qual foi?')
computador = randint(0,10)
acertou = False
palpite = 0
jogador = int(input('Qual é o seu palpite?'))
while not acertou:
    jogador = int(input('Qual é o seu palpite?'))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador :
            print('Mais... tente novamente.')
        elif jogador > computador:
            print('MEnos... tente novamente.')

print('Acertou com {} tentativas. Parabens!'.format(palpite))