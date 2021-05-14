#Escreva um script python que calcule e apresente na tela a média aritmética dos elementos da seguinte matriz:
#A = [[1,6,-9],[33,-6,88],[0,23,98]]

matriz = [[1,6,-9],[33,-6,88],[0,23,98]]
count = 0
soma = 0

for l in range(3):
    for c in range(3):
        count += 1
        soma += matriz[l][c]

media = soma / count
print("A média dos elementos da matriz é:", media)



