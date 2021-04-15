#O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta.

print('Loja quase dois - Tabela de preços:')
count=2
preço=1.99

print(f'1 produto - {preço} reais')
while count <=50:
    print(f'{count} produtos - {count*preço,2} reais')
    count+=1
