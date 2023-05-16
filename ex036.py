#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
ValorDaCasa = float(input('Digite o valor da casa R$:'))
Salario = float(input('Digite seu sálario R$:'))
TempoFinanciamento = int(input('Digite em quantos anos vai pagar:'))
prestacao = ValorDaCasa / (TempoFinanciamento * 12)
print('Para pagar uma casa de {} em {} anos é nescessário pagar uma prestaçao de R${:.2f}'.format(ValorDaCasa,TempoFinanciamento,prestacao))
if prestacao >= 0.3*Salario:
    print('\033[0;31mEMPRESTIMO NEGADO!')
else:
    print('\033[0;32mEMPRESTIMO APROVADO!')