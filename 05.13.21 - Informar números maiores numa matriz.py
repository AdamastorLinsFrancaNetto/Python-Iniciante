#Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.

matriz = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]

count = 0
for l in range(4):
    for c in range(4):
        if matriz[l][c] > 10:
            count += 1

print(f"Na matriz acima existem {count} números maiores de 10.")