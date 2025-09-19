mes = int(input('Digite um número inteiro entre 1 e 12: '))

if mes == 1:
    msg = 'Janeiro'
elif mes == 2:
    msg = 'Fevereiro'
elif mes == 3:
    msg = 'Março'
elif mes == 4:
    msg = 'Abril'
elif mes == 5:
    msg = 'Maio'
elif mes == 6:
    msg = 'Junho'
elif mes == 7:
    msg = 'Julho'
elif mes == 8:
    msg = 'Agosto'
elif mes == 9:
    msg = 'Setembro'
elif mes == 10:
    msg = 'Outubro'
elif mes == 11:
    msg = 'Novembro'
elif mes == 12:
    msg = 'Dezembro'
else:
    msg = 'Este número não representa nenhum mês'

print(msg)
