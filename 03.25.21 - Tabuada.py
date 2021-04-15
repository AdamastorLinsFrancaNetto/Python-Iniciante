#Implemente um script Python que receba um número inteiro, calcule e escreva a tabuada(de 1 a 10) desse número.

#while
n1=int(input('Informe um número inteiro: '))
cont=0
while cont <= 10:
    print(f'{n1}+{cont}={n1+cont}', end='  -  ')
    cont+=1
print('\n')
cont=0
while cont <= 10:
    print(f'{n1}-{cont}={n1-cont}', end='  -  ')
    cont+=1
print('\n')
cont=0
while cont <= 10:
    print(f'{n1}*{cont}={n1*cont}', end='  -  ')
    cont+=1
print('\n')
cont=1
while cont <= 10:
    print(f'{n1}/{cont}={round(n1/cont,2)}', end='  -  ')
    cont+=1
print("")

#for
n=int(input('Informe um número inteiro: '))
for i in range (1,11,1):
    print(f'{n} + {i} = {n+i}')
print("")
for i in range(1,11,1):
    print(f'{n} - {i} = {n-i}')
print("")
for i in range(1,11,1):
    print(f'{n} * {i} = {n*i}')
print("")
for i in range(1,11,1):
    print(f'{n} / {i} = {n/i}')

