#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base=int(input('Informe a base: '))
while base<=0:
    print('ERRO!!! o valor tem que ser maior que zero.')
    base=int(input('Informe a base: '))
expoente=int(input('Informe o expoente: '))
while expoente<=0:
    print('ERRO!!! o valor tem que ser maior que zero.')
    expoente=int(input('Informe o expoente: '))

count=1
potencia=1

while count <= expoente:
    potencia *= base
    count+=1
print('\n')
print(f'RESULTADO: {base} ^ {expoente} = {potencia}')

