A = int(input('Insira o primeiro número: '))
B = int(input('Insira o segundo número: '))
C = int(input('Insira o terceiro número: '))

if A == B and C == A:
    print('Os três valores são iguais')
elif A == B or C == A or B == C:
    print('Há dois valores iguais e um diferente')
else:
    print('Os três valores são diferentes')
