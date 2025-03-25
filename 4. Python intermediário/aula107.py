# Reduce: redução de um iterável em um valor (178)

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 25.00},
    {'nome': 'Produto 3', 'preco': 05.50},
    {'nome': 'Produto 2', 'preco': 75.99},
    {'nome': 'Produto 4', 'preco': 02.00}
]

'''
total = 0

for produto in produtos:
    total += produto['preco']

print(f'Preço total: {total}')
'''

def funcao_reduce(acumulador, produto):
    return acumulador + produto['preco']

total = reduce(funcao_reduce, produtos, 0) # Função externa (dois parâmetros) + iterável + valor inicial
print(f'Total: {total}')