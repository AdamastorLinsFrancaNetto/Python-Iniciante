#Implemente um script Python que solicite ao usuário 10 números inteiros e, ao final, informe a quantidade de números ímpares e pares lidos. Calcule também a soma dos números pares e a média dos números ímpares

#while
cont=0
contImpar=0
contPar=0
somaPar=0
somaImpar=0
while cont < 10:
    valor=int(input(f'Digite um valor {cont+1}: '))
    if valor%2 == 0 and valor !=0:
        contPar+=1
        somaPar+=valor
    elif valor%2 != 0 and valor !=0:
        contImpar+=1
        somaImpar+=valor
    cont+=1

print('Foram informados',contImpar,'números ímpares')
print('Foram informados',contPar,'números pares')
print('A soma dos números pares é:',somaPar)
if contImpar>=1:
    print('A média dos números ímpares é:',somaImpar/contImpar)

#for
contPar=0
contImpar=0
somaPar=0
somaImpar=0
for i in range(1,11):
    n=int(input(f'Informe o {i}° número: '))
    if n%2==0 and n!=0:
        contPar+=1
        somaPar+=n
    elif n%2!=0 and n!=0:
        contImpar+=1
        somaImpar+=n

print(f'Foram informados {contPar} pares.')
print(f'Foram informados {contImpar} ímpares.')
print('A soma dos números pares é:',somaPar)
if contImpar>=1:
    print('A média dos números ímpares é:',somaImpar/contImpar)
