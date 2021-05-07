#Script para incrementar de 1 um a lista numérica de tamanho qualquer informada pelo usuário

list = []
size = int(input("Qual tamanho quer a lista? "))

for i in range(size):
    n = int(input(f"Posição {i}: "))
    list.append(n)

for i in range(len(list)):
    print(f"Na posição {i} era o número {list[i]} + 1 = {list[i]+1}")
