N = int(input('Insira um número inteiro entre 100 e 200: '))

while N < 100 or N > 200:
    print('O valor é inválido.')
    N = int(input('Insira novamente um número inteiro entre 100 e 200: '))
if N > 100 or N < 200:
    print('Valor aceito. Programa finalizado')
