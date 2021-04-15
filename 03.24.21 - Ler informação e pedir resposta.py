#Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos).

sexo=str(input('Sexo: '))
esciv=str(input('Estado civil: '))

if sexo == 'F' or sexo=='f' and esciv == 'CASADA' or esciv=='casada':
    tempcasa=float(input('Informe o tempo de casada: '))
