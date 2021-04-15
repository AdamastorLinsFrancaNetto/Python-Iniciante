#Implemente um script Python que receba como entrada dois números entre 0 e 10 que representam notas de um aluno. Com base nessas notas, apresente na tela a situação do aluno, que pode ser:

nota1=float(input('Informe a primeira nota: '))
while nota1 <0 or nota1 >10:
    nota1 = float(input('Nota inválida! Informe uma nota entre 0 e 10: '))

nota2 = float(input('Informe a primeira nota: '))
while nota2 < 0 or nota2 > 10:
    nota2 = float(input('Nota inválida! Informe uma nota entre 0 e 10: '))

media=(nota1+nota2)/2

if media>=7:
    print('O aluno está APROVADO com média:',media)
elif media<4:
    print('O aluno está REPROVADO com média:',media)
else:
    print('O aluno está APTO A FINAL com média:',media)
