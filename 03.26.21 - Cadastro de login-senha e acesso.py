#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

print('CADASTRE SEU LOGIN E SENHA.')
login=str(input('Login: '))
senha=str(input('Senha: '))
while senha == login:
    print('ERRO!!! INFORME UMA SENHA DIFERENTE DO LOGIN. ')
    senha = str(input('Senha: '))
print('LOGIN E SENHA CADASTRADOS COM SUCESSO!')
print('\n')
print('INFORME LOGIN E SENHA PARA TER ACESSO AO SISTEMA.')
loginAcesso=input('Login: ')
senhaAcesso=input('Senha: ')
while login != loginAcesso or senha != senhaAcesso:
    print('ERRO!!! LOGIN OU SENHA INCORRETOS, TENTE NOVAMENTE.')
    loginAcesso = input('Login: ')
    senhaAcesso = input('Senha: ')
print('SEJA BEM VINDO!!!')