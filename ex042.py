#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
a = float(input('Digite um lado do triangulo:'))
b = float(input('Digite o outro lado do triangulo:'))
c = float(input('Digite o outro lado do triangulo'))
if a < b+c and b < a+c and c < a+b:
    if a==b and b==c and a==c:
        tipo = 'EQUILATERO'
    elif a==b or c==b or c==a:
        tipo = 'ISOCELES'
    else:
        tipo = 'ESCALENO'
    print('Os segmentos acima podem formar um triangulo {}'.format(tipo))
else:
    print('\033[1;31mOs segmentos acima NÃO PODEM formar um triangulo!')
