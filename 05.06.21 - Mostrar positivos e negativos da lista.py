# Considere o seguinte arranjo de inteiros: valores = [-3, 9, 12, -34, -2, 20, 10] Escreva um script Python que usa um laço for para percorrer todos os elementos desta matriz e exibir a soma dos valores positivos e a quantidade de valores negativos. Seu programa deverá exibir uma saída com a mensagem: A soma dos valores positivos é: 51 A quantidade de valores negativos é: 3

values = [-3, 9, 12, -34, -2, 20, 10]
somaPositivos = 0
qntNegativos = 0

for i in range(len(values)):
    if values[i] > 0:
        somaPositivos += values[i]
    if values[i] < 0:
        qntNegativos += 1

print("A soma dos valores positivos é:",somaPositivos)
print("A quantidade de números negativso é:",qntNegativos)
