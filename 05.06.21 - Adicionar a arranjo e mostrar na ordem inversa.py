# Escreva um script Python que leia 10 números inteiros e os guarde em um vetor (arranjo). Depois imprima este vetor na ordem inversa.

listNumbers = []
for i in range(0, 10, 1):
    n = int(input(f"Digite o {i+1}º número: "))
    listNumbers.append(n)

for i in range(9, -1, -1):
    print(f"Item {i} da lista é:",listNumbers[i])