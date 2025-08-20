# Armazena valor e exibe mensagem de orientação
value = int(input('Digite um número inteiro: '))

# Calculo de horas, minutos e segundos.
hours = value // 3600;

minutes = value / 60 % 60 // 1

seconds = value % 60

# Mensagem do resultado usando o método f-string para orientação
result = f'{hours} hora(s), {int(minutes)} minuto(s), {seconds} segundo(s)'

# Exibe o resultado
print(result)
