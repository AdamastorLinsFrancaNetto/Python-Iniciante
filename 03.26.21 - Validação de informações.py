#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome=str(input('Nome: '))
while len(nome) <= 3:
    print('Informe um nome com mais de 3 caracteres!')
    nome=str(input('Nome: '))
idade=int(input('Idade: '))
while idade <= 0 or idade > 150:
    print('Você deve ter de 1 a 150 anos!')
    idade=int(input('Idade: '))
salario=float(input('Salário: '))
while salario < 0:
    print('A coisa ta difícil, mas não existe salário negativo.')
    salario=float(input('Salário: '))
sexo=str(input("Sexo ('F' para feminino ou 'M' para masculino): "))
while sexo !='F' and sexo !='M':
    print("Biologicamente o sexo é 'F' ou 'M'.")
    sexo=str(input("Sexo ('F' para feminino ou 'M' para masculino): "))
estCiv=str(input('Estado civil (S, C, V ou D): '))
while estCiv !='S' and estCiv!='C' and estCiv!='V' and estCiv!='D':
    print('Informe um dos estados civis acima.')
    estCiv = str(input('Estado civil (S, C, V ou D): '))
print('\n')
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Salário: {salario} reais')
print(f'Sexo: {sexo}')
print(f'Estado cívil: {estCiv}')





