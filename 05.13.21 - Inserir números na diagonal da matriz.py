#Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais elementos. Escreva ao final a matriz obtida.

matriz = [[],
          [],
          [],
          [],
          []]

x = 0
for l in range(len(matriz)):
    for c in range(5):
        if l == x and c == x:
            matriz[c].append(1)
            x += 1
        else:
            matriz[c].append(0)

for l in range(5):
    for c in range(5):
        print(matriz[l][c], end= ' ')
    print()