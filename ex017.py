'''Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''
'''Python Exercise 17: Write a program that reads the length of the opposite leg
and the leg adjacent to a right triangle. Calculate and show the length of the hypotenuse. '''

'''a = float(input('Qual o comprimento do cateto oposto:'))
b = float(input('Qual o comprimento do cateto adjacente'))
c = ((a**2) + (b**2))**(1/2)
print('A hipotenusa vai medir {:.2f}'.format(c))'''
from math import hypot
co = float(input('Digite o comprimento do cateto oposto'))
ca = float(input('Digite o comprimento do cateto adjacente'))
hi = hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
