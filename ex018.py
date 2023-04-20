#Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
#cosseno e tangente desse ângulo.
import math
angulo = float(input('Digite o ângulo que voce deseja:'))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O angulo de {} tem o seno de {:.2f}'.format(angulo,sen))
print('O angulo de {} tem o coseno de {:.2f}'.format(angulo,cos))
print('O angulo de {} tem a atngente de {:.2f}'.format(angulo,tan))


