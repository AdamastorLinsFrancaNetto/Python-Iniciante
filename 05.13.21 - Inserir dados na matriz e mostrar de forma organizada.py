# Script para criar matriz (3x3) e receber seus elementos e usuários, apresente organizadamente a matriz na tela.

matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for l in range(3):
    for c in range(3):
        matriz[l][c] = float(input(f"Linha {l+1}, coluna {c+1}: "))

print(f" {matriz[0]} \n {matriz[1]} \n {matriz[2]}")

for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]}]', end=' ')
    print()
