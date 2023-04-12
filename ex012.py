#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input("Digite o preço do produto R$"))
d = (p*95) / 100
print("O preço do produto é {},na promoçao com 5% de desconto vai custar {:.2f}".format(p,d))
