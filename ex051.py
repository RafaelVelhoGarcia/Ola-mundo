#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
PrimeiroTermo = int(input('Digite o primeiro termo da P.A'))
razao = int(input('Digite a razão da P.A'))
decimo = PrimeiroTermo +(10-1)*razao
for c in range(PrimeiroTermo,(razao*10)+PrimeiroTermo,razao):
    print(c,end=' ')
print('ACABOU!!!')