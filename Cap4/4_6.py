LL = int(input('Insira o código LL (número inteiro com 2 dígitos)\n'))

if LL == 16:
    code = 'Bebê'
elif LL == 23:
    code = 'Infantil feminino'
elif LL == 25:
    code = 'Infantil masculino'
elif LL == 29:
    code = 'Infantil esportivo'
elif LL == 42:
    code = 'Masculino formal'
elif LL == 43:
    code = 'Masculino casual'
elif LL == 49:
    code = 'Masculino esportivo'
elif LL == 52:
    code = 'Feminino formal salto baixo'
elif LL == 53:
    code = 'Feminino formal salto alto'
elif LL == 55:
    code = 'Feminino casual salto baixo'
elif LL == 56:
    code = 'Feminino casual salto alto'
elif LL == 59:
    code = 'Feminino esportivo'
else:
    code = 'Código inviálido'

print(code)
