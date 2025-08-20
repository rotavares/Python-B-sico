# Exibe a orientação
print('Digite o nome da família')

# Orienta e armazena os nomes
mother = input('Nome da mãe: ')
father = input('Nome do pai: ')
child = input('Nome da criança: ')

# Método .format e pula uma linha
family = 'Os adultos {} e {} são responsáveis por {} \n'.format(mother, father, child)

# Exibe na tela a mensagem
print('.format: ', family)

# Método f-string
family = f'Os adultos {mother} e {father} são responsáveis por {child}'

# Exibe na tela mensagem
print('f-string: ', family)
