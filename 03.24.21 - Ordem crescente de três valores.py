#Implemente um script Python que, dado três valores A, B e C o programa os escreva em ordem crescente.

n1=int(input('Informe o primeiro número: '))
n2=int(input('Informe o segundo número: '))
n3=int(input('Informe o terceiro número: '))

if n1<n2<n3:
    print(f'A ordem crescente é {n1},{n2},{n3}')
elif n1<n3<n2:
    print(f'A ordem crescente é {n1},{n3},{n2}')
elif n2<n1<n3:
    print(f'A ordem crescente é {n2},{n1},{n3}')
elif n2<n3<n1:
    print(f'A ordem crescente é {n2},{n3},{n1}')
elif n3<n1<n2:
    print(f'A ordem crescente é {n3},{n1},{n2}')
elif n3<n2<n1:
    print(f'A ordem crescente é {n3},{n2},{n1}')
else:
    print('Algum dos números são iguais.')
