# Filtro de dados em list comprehension (filter)

'''
Anotações da aula:

    - Esquerda do 'for': mapeamento.
    - Direita do 'for': filtro.
'''

import pprint # Um print 'bonito'

def pretty_print(value):
    return pprint.pprint(value, sort_dicts=False, width=40)

lista = [numero for numero in range(10) if numero <= 5] # Filtra os números menores ou iguais a 5
pretty_print(lista)

produtos = [
    {'nome': 'Lápis', 'preco': 2.50},
    {'nome': 'Caneta', 'preco': 3.00},
    {'nome': 'Caderno', 'preco': 5.00}
]

filtro_produtos = [
    produto for produto in produtos 
    if produto['preco'] < 5.00 # Filtra apenas os produtos com preço menor que R$ 5.00
]

pretty_print(filtro_produtos)