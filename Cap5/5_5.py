LMin = int(input('Insira o valor de LMin: '))
LMax = int(input('Insira o valor de LMax: '))
D = int(input('Insira o valor de D: '))

if D <= 0:
    print(f'O valor {D} é inválido')
else:
    L = LMin
    while L < LMax:
        if L % D == 0:
            print(L)
        L = L + 1
print('Fim do programa...')
    
