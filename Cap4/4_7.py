nome = input('Nome: ')
idade = int(input('Idade: '))
sexo = input("'F' para feminino e 'M' para masculino: ")


if sexo == 'f' or sexo == 'F':
    if idade >= 21 and idade <= 34:
       retorno = 'Apta para o serviço'
    else:
        retorno = 'Não apta para o serviço'
elif sexo == 'm' or sexo == 'M':
    if idade >= 18 and idade <= 39:
        retorno = 'Apto para o serviço'
    else:
        retorno = 'Não apto para o serviço'
else:
    print("Sexo inválido, tente novamente com apenas 1 caractere 'f' ou 'm'")
