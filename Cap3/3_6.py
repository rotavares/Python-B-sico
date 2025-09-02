# Armazena o nome e o total vendido do primeiro vendedor.

fname = input('Digite o nome do vendedor: ')
fvalueseller = float(input(f'Insira o valor total que {fname} vendeu: '))

# Armazena o nome e total vendido do segundo vendedor.

sname = input('Digite o nome do vendedor: ')
svalueseller = float(input(f'Insira o valor total que {sname} vendeu: '))

# Armazena o nome e total vendido do terceiro.

tname = input('Digite o nome do vendedor: ')
tvalueseller = float(input(f'Insira o valor total que {tname} vendeu: '))


# Mensagem para informar o nome, valor total vendido e comissão do primeiro vendedor.

print(f'vendedor {fname} vendeu R$ {fvalueseller} e faz jus a uma comissão de R${fvalueseller * 0.06 + 1200:.2f}')


# Mensagem para informar o nome, valor total vendido e comissão do segundo vendedor.

print(f'vendedor {sname} vendeu R$ {svalueseller} e faz jus a uma comissão de R${svalueseller * 0.06 + 1200:.2f}')


# Mensagem para informar o nome, valor total vendido e comissão do terceiro vendedor.

print(f'vendedor {tname} vendeu R$ {tvalueseller} e faz jus a uma comissão de R${tvalueseller * 0.06 + 1200:.2f}')
