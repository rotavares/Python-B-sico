'''
Escreva um programa que leia um texto e mostre na tela o texto e a quantidade
de caracteres que ele contém, usando a seguinte mensagem:

"O texto {AquiColoqueOTexto} contém {Quantidade} caracteres"

Faça de dois modos: com o método .format() e com f-string
'''

# Printa na tela a orientação e armazena a string digitada
string = input('Digite o texto: ')

# Armazena a quantidade de caracteres
length = len(string)

# Método .format para formatar
message = '.format: O texto "{}" contém {} caracteres' .format(string, length)

# Exibe a mensagem
print(message)

# Pula uma linha e usao imétodo f-string para formatar
message = f'f-string: O texto "{string}" contém {length} caracteres'

# Exibe a mensagem
print(message)
