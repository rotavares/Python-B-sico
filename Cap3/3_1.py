'''
Escreva um programa que leia os nomes de três pessoas de uma família: mãe, pai e criança.
O programa deve exibir na tela a mensagem.

"Os adultos {mãe} e {pai} são responsáveis por {criança}"

Faça com dois modos: com o método .format() e com f-string
'''

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
