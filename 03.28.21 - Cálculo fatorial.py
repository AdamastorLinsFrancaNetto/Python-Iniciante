#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.

fatorial=int(input('Fatorial de: '))
count=fatorial+1
temp=fatorial
while count>2:
    print(f'{fatorial}! = {fatorial}',end=' . ')
    count-=1
    while count>=3:
        count-=1
        temp*=count
        print(count,end=' . ')
count-=1
print(f'{count} = {temp}')