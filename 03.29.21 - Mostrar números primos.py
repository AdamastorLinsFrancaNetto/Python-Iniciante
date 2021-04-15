#Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

nmax=int(input('Até que número deseja saber os números primos existentes? '))
count1=0
count2=1
log=bool(0)
while count1<nmax:
    count1+=1
    ntest=count1
    while count2<ntest-1:
        count2+=1
        temp=(ntest%count2==0)
        if temp==False:
            log+=0
        else:
            log+=1
    if ntest==1:
        print(ntest)
    elif log==bool(0):
        print(f'{ntest} é um número primo.')
    elif log!=bool(0):
        print(ntest)
    log=bool(0)
    count2=1
    temp=0


