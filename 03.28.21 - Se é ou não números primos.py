#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

n1=int(input('Informe um número inteiro: '))
count=1
log=bool(0)

while count<n1-1:
    count+=1
    temp=(n1%count==0)
    if temp==False:
        log+=0
    else:
        log+=1
if n1==1:
    print(f'{n1} NÃO é um número primo.')
elif log==bool(0):
    print(f'{n1} é um número primo.')
elif log!=bool(0):
    print(f'{n1} NÃO é um número primo.')
print(n1)
print(count)





