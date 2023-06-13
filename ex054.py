import datetime
cont = 0
cont2 = 0
hoje = datetime.date.today().year
for c in range(1,8):
    n = int(input('Digite em que ano a {} pessoa nasceu:'.format(c)))
    if n <= (hoje - 18):
        cont += 1
        idade = 'MENOR DE IDADE'
    #elif n ==(hoje - 18):
        #idade = 'Alcança a maioridade esse ano'
    else:
        idade = 'MAIOR DE IDADE'
        cont2 += 1
print('Ao todo tivemos {} pessoas menores de idade'.format(cont))
print('E também tivemos {} pessoas maiores de idade'.format(cont2))
