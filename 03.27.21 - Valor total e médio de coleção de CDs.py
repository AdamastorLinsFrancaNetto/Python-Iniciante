#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

coleção=int(input('Por quantos CDs é composta sua coleção: '))
count=1
total=0
while count <=coleção:
    temp=float(input(f'Informe o valor do CD{count}: '))
    total+=temp
    media=total/count
    count+=1

print(f'O valor total da coleção de CDs é: {total} reais.')
print(f'O valor médio por CD foi: {media} reais.')
