#Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.

print('=========== CAIXA REGISTRADORA ===========')
count=0
soma=0
resp='?'
while resp!='n'and resp!='N':
    count+=1
    temp=float(input(f'Produto {count}: - R$ '))
    soma+=temp
    if temp==0:
        print(f'TOTAL: R$ {soma}')
        pago=float(input('PAGO: R$ '))
        troco=pago-soma
        print(f'TROCO: R$ {round(troco,2)}')
        count=0
        soma=0
        print('-------------------------------------------')
        resp=str(input('DESEJA FAZER OUTRA OPERAÇÃO [S/N]: '))
        while resp!='n'and resp!='N' and resp!='s'and resp!='S':
            resp=str(input('RESPONDA [S/N] PARA CONTINUAR OPERANDO: '))
print('\nBOM TRABALHO!!!')