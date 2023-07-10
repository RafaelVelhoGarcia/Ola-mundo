soma = n = cont = 0
n = int(input('Digite um número [Digite 999 para PARAR!!!]'))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [Digite 999 para PARAR!!!]'))
print('Voce digitou {} numeros e a soma deles é {}'.format(cont,soma))




