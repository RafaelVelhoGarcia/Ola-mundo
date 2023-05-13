#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite qual é o salario do funcionario R$'))
if salario > 1250.00:
    print('Quem ganhava R${} passa a ganhar R${}'.format(salario,(salario * 1.1)))
else:
    print('Quem ganhava R${} passa a ganhar R${}'.format(salario,(salario * 1.5)))

