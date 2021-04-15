#A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

seq=int(input('Até que sequência de Fibonacci que saber: '))
while seq < 1:
    print('ERRO!!! Deve ser um número inteiro maior que zero!')
    seq = int(input('Até que sequência de Fibonacci que saber: '))
count=3
ultimo=1
penultimo=1
s1=('s1 = 1')
s2=('s1 = 1 \ns2 = 1')

if seq==1:
    print(s1)
elif seq==2:
    print(s2)
else:
    print(s2)
    while count <=seq:
        valor = ultimo + penultimo
        print(f's{count} = {valor}')
        penultimo = ultimo
        ultimo = valor
        count += 1





