#Implemente um script Python que receba como dado de entrada um número inteiro e apresente na tela se o dado número é par ou impar. Ou seja, desenvolva um algoritmo que avalia a paridade de um número.

n1=int(input('Digite um valor inteiro: '))

if n1%2==0:
    print(f'O valor {n1} é PAR')
else:
    print(f'O valor {n1} é ÍMPAR')
