# Dólar 19/09/2025, 15:55
D = 5.33

# Euro 19/09/2025, 15:55
E = 6.26

# Libra 19/09/2025, 15:55
L = 7.18

moeda = input('Insira qual moeda deseja comprar, "USD" | "EUR" | "GBP"\n')
if moeda == 'USD' or moeda == 'usd':
    valor = float(input(f'Valor em {moeda}: '))
    preco = valor * D
    msg = f'US$ {valor:.2f} = R$ {preco:.2f}'
    print(msg)
elif moeda == 'EUR' or moeda == 'eur':
    valor = float(input(f'Valor em {moeda}: '))
    preco = valor * E
    msg = f'€ {valor:.2f} = R$ {preco:.2f}'
    print(msg)
elif moeda == 'GBP' or moeda == 'gbp':
    valor = float(input(f'Valor em {moeda}: '))
    preco = valor * L
    msg = f'£ {valor:.2f} = R$ {preco:.2f}'
    print(msg)
else:
    print('Moeda não disponível')
