#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
cont = 1
while True:
    n = int(input('Digite um número para ver a tabuada'))
    if n < 0:
        break
    cont = 1
    print('-' * 40)
    while cont <= 10:
        print('{} x {} = {}'.format(n,cont,(n*cont)))
        cont += 1
    print('-' * 40)
print('PROGRAMA DE TABUADA ENCERRADA!')