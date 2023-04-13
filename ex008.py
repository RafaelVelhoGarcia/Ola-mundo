#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n = float(input('Digite uma distância em metros'))
k = n/1000
h = n/100
d = n/10
dc =n*10
c = n*100
m = n*1000
print("A distancia é {}m,{}km,{}hm,{}dm,{}dc,{}cm e {}mm".format(n,k,h,d,dc,c,m))