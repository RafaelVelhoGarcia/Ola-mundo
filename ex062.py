cont = 1
PrimeiroTermo = int(input('Digite o primeiro termo da P.A:'))
razao = int(input('Digite a razão da P.A:'))
termo = PrimeiroTermo
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} ->'.format(termo),end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais:'))
print('FIM')



