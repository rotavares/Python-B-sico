import math

# Armazena três números reais em objetos
A = float(input('A: '))
B = float(input('B: '))
C = float(input('C: '))

# Calcula seis fórmulas com os três objetos
R1 = A + B + C
R2 = A * B * C
R3 = 2 * (A + B) - C
R4 = A + B + C / 3
R5 = (2 * B) + (3 * C) / (5 * A)
R6 = math.pow(A, 2) + math.pow(B, 2)

# Exibe no terminal com uma separação " | " entre os resultados
print('R1 = {:.3f}'.format(R1),
      'R2 = {:.3f}'.format(R2),
      'R3 = {:.3f}'.format(R3),
      'R4 = {:.3f}'.format(R4),
      'R5 = {:.3f}'.format(R5),
      'R6 = {:.3f}'.format(R6),
      sep=" | ")
