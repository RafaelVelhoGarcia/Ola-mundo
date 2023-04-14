#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
#n = int(input('Digite um número'))
#d = 2*n
#t = 3*n
#r = n**(1/2)
#print('Analisando o número {} o seu dobro é {} e seu triplo é {} e sua raiz quadrada é {}'.format(n,d,t,r))

n = int(input('digite um numero'))
print('analisando o numero {} o seu dobro {} e seu triplo é {} e sua raiz quadra é {:.2f}'.format(n,(n*2),(n*3),(n**(1/2))))