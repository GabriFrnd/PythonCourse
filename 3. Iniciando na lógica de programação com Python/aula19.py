# ID, a identidade do valor que está na memória

# Variáveis com o mesmo valor:

variavel = 'A'
outra_variavel = 'A'

print(f'ID: {id(variavel)}')
print(f'ID: {id(outra_variavel)}')

# Variável com valor diferente:

numero = 123
print(f'ID: {id(numero)}')