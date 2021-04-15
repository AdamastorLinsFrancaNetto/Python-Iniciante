#Faça um programa que leia 5 números e informe o maior número.
#Faça um programa que leia 5 números e informe a soma e a média dos números.

primeiro=int(input('Número 1: '))
maior=primeiro
count=1
soma=primeiro

while count <5:
    count+=1
    temp=int(input('Número %d: '%count))
    soma+=temp
    if temp > maior:
        maior=temp

media=soma/count

print('O maior número é:',maior)
print('A soma entre os números é:',soma)
print('A média entre os números é:',media)





