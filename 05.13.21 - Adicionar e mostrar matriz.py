# Faça um programa que preenche uma matriz com o produto do valor da linha e da coluna de cada elemento. Em seguida, imprima na tela a matriz

matriz = [[],
          [],
          []]

for l in range(len(matriz)):
    for c in range(3):
        n = int(input(f"Linha {l+1}, coluna {c+1}: "))
        matriz[l].append(n)

for l in range(3):
    for c in range(3):
        print(f"[{matriz[l][c]}]", end=" ")
    print()