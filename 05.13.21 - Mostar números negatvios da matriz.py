#Escreva um script python que calcule e apresente na tela a média aritmética dos elementos da seguinte matriz:
#A = [[1,6,-9],[33,-6,88],[0,23,98]]

matriz = [[1,6,-9],[33,-6,88],[0,23,98]]
count = 0

for l in range(3):
    for c in range(3):
        if matriz[l][c] < 0:
            count += 1

print(f"Dentre os elementos da matriz {count} são menores que 0.")