aluno = input('Nome aluno: ')
nota1 = float(input('1 Nota: '))
nota2 = float(input('2 Nota: '))
nota3 = float(input('3 Nota: '))

if nota1 + nota2 + nota3 / 3 >= 7.0:
    print('Aprovado')
else:
    print('Reprovado')
