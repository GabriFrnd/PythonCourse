# map, partial, GeneratorType e esgotamento de iterators (176)

from functools import partial
from types import GeneratorType

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 25.00},
    {'nome': 'Produto 3', 'preco': 05.50},
    {'nome': 'Produto 2', 'preco': 75.99},
    {'nome': 'Produto 4', 'preco': 02.00}
]

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

def aumentar_preco(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez = partial(aumentar_preco, porcentagem = 1.1) # Cria uma nova função a partir de outra

'''
novos_produtos = [
    {**produto, 'preco': aumentar_dez(produto['preco'])}
    for produto in produtos
]
'''

def mudar_preco(produto):
    return {**produto, 'preco': aumentar_dez(produto['preco'])}

# Mapeamento: mapear de um dado para outro

novos_produtos = map(mudar_preco, produtos) # Função externa + iterável
print_iter(produtos)

print_iter(novos_produtos)
print(isinstance(novos_produtos, GeneratorType)) # Verifica se 'novos_produtos' é uma instância de 'GeneratorType'