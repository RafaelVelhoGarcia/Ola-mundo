#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
print('='*5,'LOJA DO RAFAEL','='*5)
preco = float(input('Digite o preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartao
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')
opcao = int(input('Qual a opção escolhida? '))
if opcao == 1:
    valor = preco*0.90
elif opcao == 2:
    valor = preco*0.95
elif opcao == 3:
    valor = preco
    print('Sua compra será parcelada em 2x de {.:2f} sem juros.'.format(valor/2))
elif opcao == 4:
    valor = preco*1.2
    parcela = int(input('Quantas parcelas?'))
    print('Sua compra será parcelada em {}x de {:.2f} com juros'.format(parcela,valor/parcela))
else:
    valor = preco
    print('Essa opção de pagamento \033[1;31mNÃO EXISTE\033[m.')
print('Sua compra de R${} vai custar R${} no final'.format(preco,valor))