# Crie um arranjo com vinte valores inteiros e inicialize-os aleatoriamente (não precisa ler com input(), inicialize no próprio código). Depois varra esse arranjo e imprima apenas os elementos de índice par.

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print("Os números pares da lista são:")
for i in range(len(list)):
    if list[i] % 2 == 0:
        print(list[i])