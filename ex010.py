##Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
dinheiro = float(input("Digite seu saldo atual R$"))
dollar = dinheiro / 3.27
print("Voce tem {} de saldo e pode comprar {:.2f} dolares".format(dinheiro,dollar))

