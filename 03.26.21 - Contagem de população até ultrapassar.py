#Supondo que a população de um país A seja 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

habA=int(input('Infomre o número de habitantes da população A: '))
taxaA=float(input('Taxa de crescimento anual: '))
habB=int(input('Infomre o número de habitantes da população B: '))
taxaB=float(input('Taxa de crescimento anual: '))

cont=0
while habA < habB:
    print(f'{cont} anos.')
    print(f'País A: {round(habA,0)} habitantes.')
    print(f'País B: {round(habB,0)} habitantes.')
    cont+=1
    habA=((taxaA/100)*habA)+habA
    habB=((taxaB/100)*habB)+habB
    print('\n')
print('\n')
print(f"Após {cont} anos a população 'A' atingiu {round(habA,0)} habitantes e ultrapssou a população 'B' com população {round(habB,0)} habitantes, com diferença de {round(habA-habB,0)} habitantes.")
