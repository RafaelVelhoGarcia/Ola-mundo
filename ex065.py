#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
condi = False
soma = cont = 0
while condi is False:
    n = int(input('Digite um número:'))
    soma += n
    cont += 1
    continuar = str(input('Voce quer continuar [S / N]')).upper().strip()[0]
    if continuar == 'N':
        condi = True
    if cont == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print('Voce digitou {} números e a media foi de {:.2f}'.format(cont,(soma/cont)))
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))












