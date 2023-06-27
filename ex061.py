#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
cont = 1
PrimeiroTermo = int(input('Digite o primeiro termo da P.A:'))
razao = int(input('Digite a razão da P.A:'))
termo = PrimeiroTermo
while cont <= 10:
    print('{} ->'.format(termo),end='')
    termo += razao
    cont += 1
print('FIM')