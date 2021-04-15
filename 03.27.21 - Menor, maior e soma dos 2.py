#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

n=int(input('Quantos números: '))
primeiro=int(input('Número 1: '))
while primeiro <0 or primeiro >1000:
    print('ERRO!!! Informe números entre 0 e 1000.')
    primeiro=int(input('Número 1: '))
maior=primeiro
menor=primeiro
count=2
while count <= n:
    temp=int(input('Número %d: '%count))
    while temp <0 or temp>1000:
        print('ERRO!!! Informe números entre 0 e 1000.')
        temp=int(input('Número %d: ' % count))
    count += 1
    if temp>maior:
        maior=temp
    elif temp<menor:
        menor=temp
print('O maior número é:',maior)
print('O menor número é:',menor)
print(f'A soma do maior ({maior}) e do menor ({menor}) é igual a {maior+menor}.')
