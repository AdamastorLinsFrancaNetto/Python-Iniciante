#Implemente um script Python que consista em uma calculadora básica de quatro operações (soma, subtração, multiplicação e divisão)

sn='s'
while sn == 's':
    n1=float(input('\nNúmero: '))
    op=str(input('+ - * /: '))
    while op != '+' and op != '-' and op != '*' and op != '/':
        op=str(input('Informe uma das alternativas + - * /: '))
    n2=float(input('Número: '))

    if op == '+':
        print(f'RESULTADO: {n1} + {n2} = {n1+n2}')
    elif op == '-':
        print(f'RESULTADO: {n1} - {n2} = {n1-n2}')
    elif op == '*':
        print(f'RESULTADO: {n1} * {n2} = {n1*n2}')
    elif op == '/':
        print(f'RESULTADO: {n1} / {n2} = {n1/n2}')

    sn=str(input('\nDeseja fazer outra operação [s/n]? '))
    while sn != 's' and sn != 'S' and sn != 'n' and sn != 'N':
        sn=str(input('Deseja fazer outra operação [s/n]? '))
print('\nVOLTE SEMPRE!!!')

#for
for x in iter(int, 1):
    pass
    n1=float(input('\nNúmero: '))
    op=str(input('+ - * / : '))
    while op != '+' and op != '-' and op != '*' and op != '/':
        op=str(input('Informe uma das alternativas + - * / : '))
    n2=float(input('Número: '))
    if op == '+':
        print(f'RESULTADO: {n1} + {n2} = {n1+n2}')
    elif op == '-':
        print(f'RESULTADO: {n1} - {n2} = {n1-n2}')
    elif op == '*':
        print(f'RESULTADO: {n1} * {n2} = {n1*n2}')
    elif op == '/':
        print(f'RESULTADO: {n1} / {n2} = {n1/n2}')
    sn=str(input('\nDeseja fazer outra operação [S/N]? '))
    while sn != 's' and sn != 'S' and sn != 'n' and sn != 'N':
        sn=str(input('Deseja fazer outra operação [S/N]? '))
    if sn != 's' and sn != 'S':
        break
print('\nVOLTE SEMPRE !!!')




