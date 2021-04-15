#Escreva um algoritmo que leia o número de identificação, as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação, e calcule a média de aproveitamento.

aluno=str(input('Informe o número de identificação do aluno: '))

if aluno == "2021111510043":
    print('Olá, Adamastor Lins Franca Netto')
else:
    print('Informe um número de identificação válido!')

nt1=float(input('Informe a primeira nota: '))
nt2=float(input('Informe a segunda nota: '))
nt3=float(input('Informe a terceira nota: '))
medex=float(input('Informe a media do exercícios: '))

meda=(nt1+(nt2*2)+(nt3*3)+medex)/7
print()
if meda >= 9:
    print('A média de aproveitamento foi {} que corresponde a "A"'.format(round(meda,1)))
elif meda >= 7.5 and meda < 9:
    print('A média de aproveitamento foi {} que corresponde a "B"'.format(round(meda,1)))
elif meda >= 6 and meda < 7.5:
    print('A média de aproveitamento foi {} que corresponde a "C"'.format(round(meda,1)))
elif meda >= 4 and meda < 6:
    print('A média de aproveitamento foi {} que corresponde a "D"'.format(round(meda,1)))
else:
    print('A média de aproveitamento foi {} que corresponde a "E"'.format(round(meda,1)))

