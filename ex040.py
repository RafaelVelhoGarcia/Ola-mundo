#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
NotaUm = float(input('Digite a primeira nota:'))
NotaDois = float(input('Digite a segunda nota:'))
media = (NotaUm + NotaDois)/2
print('Tirando {} e {},a média é {:.1f}'.format(NotaUm,NotaDois,media))
if media < 5:
    print('\033[31mO aluno está REPROVADO')
elif 5 <= media < 6.9 :
    print('\033[33mO aluno está de RECUPERAÇÃO')
else:
    print('\033[32m O aluno está APROVADO')

