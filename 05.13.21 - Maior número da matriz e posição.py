# Leia uma matriz 4 x 4, imprima a matriz e retorne à localização (linha e a coluna) do maior valor

matriz = [[10,20,30,40],
          [1,2,3,4],
          [100,200,300,400],
          [-10,-20,-30,-40]]

maior = 0
maiorL = 0
maiorC = 0

for l in range(len(matriz)):
    for c in range(len(matriz)):
        if matriz[l][c] > maior:
            maior = matriz[l][c]
            maiorL = l
            maiorC = c

for l in range(len(matriz)):
    for c in range(len(matriz)):
        print(f"[{matriz[l][c]}]", end=" ")
    print()

print("O maior número é:",maior)
print("Está na linha:",maiorL+1)
print("Está na coluna:",maiorC+1)