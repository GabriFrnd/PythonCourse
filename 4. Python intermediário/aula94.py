# Exercício: três em um (160)

'''
    Aumente os preços dos produtos a seguir em 10%
    Gere 'novos_produtos' por deep copy
'''

import copy

produtos = [
     {'nome': 'Produto 5', 'preco': 10.00},
     {'nome': 'Produto 1', 'preco': 22.32},
     {'nome': 'Produto 3', 'preco': 10.11},
     {'nome': 'Produto 2', 'preco': 105.87},
     {'nome': 'Produto 4', 'preco': 69.90},
]

aumento_preco = [
    {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
    for produto in copy.deepcopy(produtos)
]

print(*aumento_preco, sep='\n')

'''
    Ordene os produtos por nome decrescente
    Gere 'produtos_ordenados_por_nome' por deep copy 
'''

print()
produtos.sort(key=lambda item: item['nome'], reverse=True)

for item in copy.deepcopy(produtos):
    print(item)

'''
    Ordene os produtos por preço crescente
    Gere 'produtos_ordenados_por_preco' por deep copy
'''

print()
produtos.sort(key=lambda item: item['preco'])

for item in copy.deepcopy(produtos):
    print(item)