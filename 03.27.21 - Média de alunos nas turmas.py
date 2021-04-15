#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

turmas=int(input('Quantas turmas tem na faculdade: '))
count=1
alunos=0
print('\n')
while count <=turmas:
    temp=int(input(f'Quantos alunos tem na turma {count}: '))
    alunos+=temp
    media=alunos/count
    count+=1
print('\n')
print(f'Nas {turmas} turmas da faculdade tem um total de {alunos}, que da uma média de {media} alunos por turma.')
