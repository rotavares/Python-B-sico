produto = float(input('Preço de custo do Produto: '))

if produto <= 100.00:
    margem = produto * 0.45
else:
    margem = produto * 0.35

valorFinal = produto + margem

mensagem = f'Preço de venda: {valorFinal:.2f}'
print(mensagem)
