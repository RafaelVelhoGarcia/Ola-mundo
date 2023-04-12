#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
l = float(input("digite a largura da parede"))
h = float(input("digite a altura da parede"))
area = h*l
print("A largura da parede é de {}m e sua altura é {}m e sua area é de {} para pinta-la serao nescessarios {}litros de tinta".format(l,h,area,(area/2)))
