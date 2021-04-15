#Implemente um script Python que recebe 3 números reais do teclado e verificar se o primeiro é maior que a soma dos outros dois.

n1=int(input('Informe o primeiro número: '))
n2=int(input('Informe o segundo número: '))
n3=int(input('Informe o terceiro número: '))

n2n3=n2+n3
print(f'A soma entre {n2} e {n3} é igual a {n2n3}')

if n1 > n2n3:
    print(f'O número {n1} é MAIOR que a soma entre o {n2} e {n3}.')
elif n1 < n2n3:
    print(f'O número {n1} é MENOR que a soma entre o {n2} e {n3}.')
else:
    print(f'O número {n1} é IGUAL que a soma entre o {n2} e {n3}.')
