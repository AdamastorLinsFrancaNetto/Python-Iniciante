#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

dias=int(input('Quantos dias de informações meteorológicas? '))
primeiro=float(input('Informe a temperatura do dia 1: '))
menor=primeiro
maior=primeiro
soma=0
count=1

while count < dias:
    count+=1
    temp=float(input(f'Informe a temperatura do dia {count}: '))
    soma += temp
    if temp>maior:
        maior=temp
    elif temp<menor:
        menor=temp
    soma+=temp
media=soma/dias
print('A temperatura máxima foi:',maior)
print('A temperatura mínima foi:',menor)
print('A temperatura média foi:',media)
