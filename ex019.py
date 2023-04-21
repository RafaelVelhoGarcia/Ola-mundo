#Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
a = input('Digite o primeiro aluno:')
b = input('Digite o segundo aluno:')
c = input('Digite o terceiro aluno:')
d = input('Digite o quarto aluno:')
lista = [a,b,c,d]
escolhido = choice(lista)
print('O aluno escolhido foi {} '.format(escolhido))

