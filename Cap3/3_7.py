# Armazena o valor do investimento.

totalinvestiment = float(input('Insira o valor do investimento: '))

# Armazena o valor do custo.

cost = float(input('Insira o valor do custo: '))

# Armazena o valor da receita.

netincome = float(input('Insira o valor da receita: '))

# Variável 'roi' que armazena o cálculo do Retorno sobre o investimento.

roi = (netincome - (totalinvestiment + cost)) / (totalinvestiment + cost) * 100

# Retorna na tela o valor da variavél 'roi'.

print(f'ROI = {roi:.1f}%')
