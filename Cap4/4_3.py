salario = float(input('Salário: '))
parcela = float(input('Parcela: '))
if parcela <= salario * 0.08:
    print('Empréstimo concedido')
else:
    print('Empréstimo não concedido')
