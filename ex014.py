#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius
# e converta para graus Fahrenheit.
c = float(input("Informe a temperatura em C"))
f = (9*c +160)/5
print('A temperatura {:.2f}C corresponde a temperatura{:.2f}F'.format(c,f))
