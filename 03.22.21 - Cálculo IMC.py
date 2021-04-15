#A fórmula é IMC = peso / ( altura )2 Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição de acordo com a tabela abaixo.

peso=float(input('Peso: '))
altu=float(input('Altura: '))

imc=peso/(altu)**2

print(f'Seu IMC é: {round(imc,1)}')

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >=18.5 and imc <25:
    print('Você está no peso ideal')
elif imc >= 25 and imc < 30:
    print('Você está acima do peso')
else:
    print('Você está obeso')
