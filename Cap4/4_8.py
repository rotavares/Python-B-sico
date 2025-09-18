ano = int(input('Insira o ano, exemplo: 2001\n'))

if ano % 4 == 0 and ano % 100 == 0 or ano % 400 == 0:
    print(f'{ano} não é bissexto')
else:
    print(f'{ano} é bissexto')
