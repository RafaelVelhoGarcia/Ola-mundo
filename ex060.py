#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
numero = int(input('Digite um número para calcular o fatorial:'))
c = numero
f = 1
print('Calculando {}!'.format(numero),end='')
while c > 0:
    print('  {} '.format(c),end=' ')
    print(' X' if c > 1 else '=',end= '')
    f *= c
    c -= 1
print(' {}'.format(f))
