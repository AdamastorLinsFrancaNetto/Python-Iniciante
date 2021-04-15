#Implemente um script Python que leia um número n inteiro e apresente a soma de todos os números de 1 até n. Faça isso usando o laço while.
n=int(input('Informe um número: '))

#while
cont=0
while cont < n+1:
    print(f'{n} + {cont} = {cont+n}')
    cont+=1

#for
n=int(input('Infomre um valor inteiro: '))
for i in range (0,n+1,1):
    print(f'{i} + {n} = {i+n}')