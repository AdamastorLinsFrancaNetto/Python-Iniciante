# Faça um algoritmo que leia 5 temperaturas (valores válidos: –15.0° a 45.0°) e armazene-as em um vetor. Em seguida, crie um novo vetor que guardará as informações na temperatura fahrenheit e imprima seu valores.

listTempCelsius = []
for i in range(5):
    t = float(input(f"Informe a {i+1}ª temperatura em Celsius: "))
    listTempCelsius.append(t)

print("Lista de temperatura em graus Celsius:")
for i in range(len(listTempCelsius)):
    print(f"Posição {i} = {listTempCelsius[i]}ºC")
print("")

listTempFahrenheit = []
for i in range(len(listTempCelsius)):
    c = (listTempCelsius[i]*9/5)+32
    listTempFahrenheit.append(c)

print("Lista de temperatura em graus Fahrenheit:")
for i in range(len(listTempFahrenheit)):
   print(f"Posição {i} = {listTempFahrenheit[i]}ºF")

