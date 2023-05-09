#Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
vel = float(input('Qual é a velocidade atual do carro?'))
multa = (vel - 80)*7
if vel > 80:
    print('MULTADO!!! Voce excedeu o limite de velocidade permitido que é 80km/h ')
    print('Voce deve pagar uma multa de {:.2f}R$'.format(multa))
print('Tenha um bom dia,dirija com segurança')



