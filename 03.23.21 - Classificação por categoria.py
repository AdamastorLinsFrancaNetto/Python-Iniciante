#Implemente um script Python que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:

idade=int(input('Informe a idade do nadador: '))

print('CATEGORIAS:'
'\n -INFANTIL A: 5 a 7 anos'
'\n -INFANTIL B: 8 a 10 anos'
'\n -JUVENIL A: 11 a 13 anos'
'\n -JUVENIL B: 14 a 17 anos'
'\n -SÊNIOR: maiores de 18 anos')

if idade >=5 and idade <=7:
    print('O nadador é da categoria INFANTIL A.')
elif idade >=8 and idade <=10:
    print('O nadador é da categoria INFANTIL B.')
elif idade >= 11 and idade <=13:
    print('O nadador é da categoria JUVENIL A.')
elif idade >= 14 and idade <= 17:
    print('O nadador é da categoria JUVENIL B.')
elif idade >= 18:
    print('O nadador é da categoria SÊNIOR.')
else:
    print('Não tem categorias para abaixo de 5 anos.')
