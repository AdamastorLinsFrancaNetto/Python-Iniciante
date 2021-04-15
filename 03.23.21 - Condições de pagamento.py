#Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.

preco=float(input('Informe o preço normal: '))

print('Condição de pagamento'
'\n 1 À vista em dinheiro ou cheque, recebe 10% de desconto'
'\n 2 À vista no cartão de crédito, recebe 15% de desconto'
'\n 3 Em duas vezes, preço normal de etiqueta sem juros'
'\n 4 Em mais de duas vezes, preço normal de etiqueta mais juros de 10%')

cond=int(input('Informe a condição de pagamento: '))

if cond == 1:
    print('O valor a ser pago é:',preco*.90)
elif cond == 2:
    print('O valor a ser pago é:',preco*.85)
elif cond==3:
    print('O valor a ser pago é:',preco,'em 2x de',preco/2)
elif cond==4:
    print('O valor a ser pago é:',(preco*.10)+preco,'em ate 10x')
else:
    print('Informe uma das condições acima.')
