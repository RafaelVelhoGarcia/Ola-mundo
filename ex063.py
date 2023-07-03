#Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci
print('Sequencia de fibonacci')
cont = 3
n = int(input('Digite qauntos termos voce quer mostrar:'))
t1 = 0
t2 = 1
t3 = t1 + t2
print(t1,t2,end=' ')
while cont != n:
    cont +=1
    print('{}'.format(t3),end=' ')
    t1 = t2
    t2 = t3
    t3 = t1 + t2
