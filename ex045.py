from time import sleep
import random
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1.5)
print('PO!!!')
lista = [0,1,2]
escolha = random.choice(lista)
if escolha == jogada:
    resultado = '\033[1;33mIMPATOU!'
    if jogada == 0:
        jogador = 'PEDRA'
    elif jogada == 1:
        jogador = 'PAPEL'
    elif jogada == 2:
        jogador = 'TESOURA'
    computador = jogador
elif jogada == 0 and escolha == 1 or jogada == 1 and escolha == 2 or jogada == 2 and escolha == 0:
    resultado = '\033[1;31mPERDEU!'
    if jogada == 0:
        jogador = 'PEDRA'
        computador = 'PAPEL'
    elif jogada == 1:
        jogador = 'PAPEL'
        computador = 'TESOURA'
    elif jogada == 2:
        jogador = 'TESOURA'
        computador = 'PEDRA'
else:
    if jogada == 0:
        jogador = 'PEDRA'
        computador = 'TESOURA'
    elif jogada == 1:
        jogador = 'PAPEL'
        computador = 'PEDRA'
    elif jogada == 2:
        jogador = 'TESOURA'
        computador = 'PAPEL'
    resultado = '\033[1;32mGANHOU!'
print('-=-'*10)
print('O COMPUTADOR JOGOU {}'.format(computador))
print('O JOGADOR JOGOU {}'.format(jogador))
print('-=-'*10)
print('O JOGADOR {}'.format(resultado))
