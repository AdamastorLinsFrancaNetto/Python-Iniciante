#Escreva um script Python que declara um vetor de dez elementos do tipo int. Em seguida, use um laço for para solicitar ao usuário que insira dez valores inteiros e armazene tais valores no vetor. Por fim, use novamente um laço for para varrer o arranjo e imprimir os valores múltiplos de dois na tela.

list = []
for i in range (10):
    n = int(input(f"Posição {i}: "))
    list.append(n)

print("Dos números citados acimaestes estes são multiplos de 2:")
for i in range (len(list)):
    if list[i] %2 == 0:
        print(list[i])
