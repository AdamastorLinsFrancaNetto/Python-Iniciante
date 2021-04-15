#Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal.

sexo=str(input('Sexo: '))
altu=float(input('Altura: '))

idm=(72.7*altu)-58
idf=(62.1*altu)-44.7

if sexo =='F' or sexo =='FEMININO' or sexo =='f' or sexo =='feminino':
    print('O peso ideal para mulheres de sua altura é:',idf)
elif sexo =='M' or sexo =='MASCULINO' or sexo=='m' or sexo=="masculino":
    print('O peso ideal para homens de sua altura é:', idm)
else:
    print('Sexo inválido, corrija para prosseguir.')