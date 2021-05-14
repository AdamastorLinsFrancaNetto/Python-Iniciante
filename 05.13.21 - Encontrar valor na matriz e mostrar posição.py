#Leia uma matriz 5 x 5. Leia também um valor ´ X. O programa deverá fazer uma busca desse valor na matriz e, ao final, escrever a localização (linha e coluna) ou uma mensagem de “não encontrado”.

matriz = [[1,2,3,4,5],
          [6,7,8,9,10],
          [11,12,13,14,15],
          [16,17,18,19,20],
          [21,22,23,24,25]]

for l in range(len(matriz)):
    for c in range(len(matriz)):
        print(f"[{matriz[l][c]}]", end=" ")
    print()

search = int(input("Informe o valor que desejas procurar na matriz: "))
count = 0

for l in range(len(matriz)):
    for c in range(len(matriz)):
        if matriz[l][c] == search:
            print(f"O valor está na linha {l+1} e coluna {c+1}.")
        else:
            count += 1
if count == (len(matriz)*len(matriz)):
    print("Valor não encontrado!")