#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input("Digite o salario do funcionario R$"))
a = s*1.15
print('Um funcionario que ganhava R${},com 15% de aumento,passa a ganhar R${:.2f}'.format(s,a))
