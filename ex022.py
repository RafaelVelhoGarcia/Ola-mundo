#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

nome = str(input('Digite seu nome completo')).strip()
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letra'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0],len(separa[0])))


