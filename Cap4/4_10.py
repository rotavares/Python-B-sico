A = float(input('Primeiro lado: '))
B = float(input('Segundo lado: '))
C = float(input('Terceiro lado: '))

if A > 0 and B > 0 and C > 0:
    if A + B > C or A + C > B or B + C > A:
        if A == B and A == C:
            print('Equilatero')
        elif A == B or A == C or B == C:
            print('Isósceles')
        else:
            print('Escaleno')
else:
    print('Não é um triangulo')
