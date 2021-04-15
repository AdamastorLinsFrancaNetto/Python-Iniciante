#Implemente um script Python que receba como entrada cinco números e informe quantos desses números são maiores que 10.

n1=float(input('Informe o primeiro valor: '))
n2=float(input('Informe o segundo valor: '))
n3=float(input('Informe o terceiro valor: '))
n4=float(input('Informe o quarto valor: '))
n5=float(input('Informe o quinto valor: '))

if n1>10:
    n11=1
elif n1<=10:
    n11=0
if n2>10:
    n22=1
elif n2<=10:
    n22=0
if n3>10:
    n33=1
elif n3<=10:
    n33=0
if n4>10:
    n44=1
elif n4<=10:
    n44=0
if n5>10:
    n55=1
elif n5<=10:
    n55=0

print('Dos 5 números apresentados {} são maiores que 10.'.format(n11+n22+n33+n44+n55))
