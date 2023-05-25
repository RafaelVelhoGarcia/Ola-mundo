#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
peso = float(input('Qual o seu peso?kg:'))
altura = float(input('Qual a sua altura?m:'))
imc = peso / altura**2
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5 :
    status = 'ABAIXO DO PESO IDEAL'
elif imc < 25:
    status = '\033[1;32mPESO IDEAL'
elif imc <= 30:
    status = 'SOBRE PESO'
elif imc <= 40:
    status = 'OBESIDADE'
else:
    status = '\033[1;31mOBESIDADE MORBIDA'
print('Voce está em {}'.format(status))
