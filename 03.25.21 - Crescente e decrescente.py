#Implemente um script Python que escreva na tela todos os números de 1 até 50 de forma crescente e depois decrescente.

#while
i=1
while i<=50:
    print(i, end=', ')
    i=i+1
print('')
i=50
while i>=1:
    print(i, end=', ')
    i=i-1
print('')
#for
for i in range(1, 51, 1):
    print(i, end=", ")
print('')
for i in range(50, 0, -1):
    print(i, end=", ")

