#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formar um triângulo.
print('-=-'* 10)
print('ANALISADOR DE TRIANGULOS')
print('-=-'* 10)
a = int(input('Primeiro segmento:'))
b = int(input('Segundo segmento:'))
c = int(input('Terceiro segmento:'))

if a > b+c and b > a+c and c > b+a:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIANGULO')
else:
    print('Os segmentos acima PODEM formar um triangulo')
