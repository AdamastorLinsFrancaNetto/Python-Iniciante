#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

eleitores=int(input('Quantos eleitores iram participar: '))
print('CANDIDATOS:\n17 - Bolsonaro\n13 - Haddad\n12 - Ciro')
count=1
Bolsonaro=0
Haddad=0
Ciro=0
while count <=eleitores:
    voto=input(f'Eleitor N{count} qual seu voto: ')
    if voto == '17':
        Bolsonaro+=1
    elif voto == '13':
        Haddad+=1
    elif voto == '12':
        Ciro+=1
    else:
        print('ERRO!!! Vote em um dos candidatos:\n17 - Bolsonaro\n13 - Haddad\n12 - Ciro.')
        voto = input(f'Eleitor N{count} qual seu voto: ')
        if voto == 17:
            Bolsonaro += 1
        elif voto == 13:
            Haddad += 1
        elif voto == 12:
            Ciro += 1
        else:
            print('ERRO!!! Vote em um dos candidatos:\n17-Bolsonaro\n13-Haddad\n12-Ciro.')
    count+=1
print('\n')
print(f'Bolsonaro obteve {Bolsonaro} votos.')
print(f'Haddad obteve {Haddad} votos.')
print(f'Ciro obteve {Ciro} votos.')









