# Escreva um script Python que leia um vetor A de 10 elementos inteiros e um valor qualquer inteiro X. Em seguida, realize uma busca no arranjo a fim de verificar se o valor X existe no imprima na tela "ACHEI" se o valor X existir em A e "NAO ACHEI" caso contrário.

listNumbers = []
for i in range(10):
    n = int(input(f"Informe o elemento {i} para a lista: "))
    listNumbers.append(n)

search = int(input("Qual item queres verificar se está incluso na lista? "))
count = 0

for i in range(len(listNumbers)):
    if listNumbers[i] == search:
        print(f"Achei! Está na posição {i} da lista.")
    else:
        count+=1
if count == len(listNumbers):
    print("Não achei na lista!")

