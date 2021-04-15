#Implemente um script Python que receba como entrada dois valores numéricos e apresente a diferença do maior pelo menor.

n1=float(input('Informe o primeiro número: '))
n2=float(input('Informe o segundo número: '))

if n1>n2:
    print(f'O primeiro número é maior que o segundo, logo a diferença é: {n1-n2}')
else:
    print(f'O segundo número é maior que o primeiro, logo a diferença é: {n2-n1}')
