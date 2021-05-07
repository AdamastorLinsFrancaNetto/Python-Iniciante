# Escreva um programa para ler um vetor de 10 elementos inteiros. Em seguida exclua o 3° elemento do vetor deslocando os elementos subsequentes uma posição para o inicio do vetor. Depois escreva o vetor resultante na tela.

list = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(list)):
    print(f"Posição {i}: {list[i]}")

del(list[2])

print("Com a exclusão do 3º elemento da lista ela ficou com a seguinte composição: ")
for i in range(len(list)):
    print(f"Posição {i}: {list[i]}")