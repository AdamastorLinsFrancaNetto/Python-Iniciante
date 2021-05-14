#Leia duas matrizes 4 x 4 e escreva uma terceira com os maiores valores de cada posição das matrizes lidas

matriz1 = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12],
           [13,14,15,16]]

matriz2 = [[16,15,14,13],
           [12,11,10,9],
           [8,7,6,5],
           [4,3,2,1]]

matriz3 = [[],
           [],
           [],
           []]

for l in range(4):
    for c in range(4):
        if matriz1[l][c] > matriz2[l][c]:
            matriz3[l].append(matriz1[l][c])
        else:
            matriz3[l].append(matriz2[l][c])

for l in range(4):
    for c in range(4):
        print(f"[{matriz3[l][c]}]", end=" ")
    print()