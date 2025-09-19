municipio = input('Nome do município: ')
eleitores = int(input('Quantidade de eleitores: '))
votos = int(input('Quantidade de votos do candidato mais votado: '))

if votos < eleitores * 0.5:
    msg = 'Haverá segundo turno'
else:
    msg = 'Não haverá segundo turno'

print(msg)
