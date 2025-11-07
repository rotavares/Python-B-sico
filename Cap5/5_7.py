soma = qtde = 0
numero = 1
while numero != 0:
    numero = int(input('Insira um número inteiro: '))
    if numero != 0:
        soma = soma + numero
        qtde = qtde + 1
print(f'soma = {soma}')
