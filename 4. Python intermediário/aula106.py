# Filter: um filtro funcional (177)

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

'''
novos_produtos = [
    produto for produto in produtos
    if produto['preco'] >= 10
]
'''

novos_produtos = filter( # Função externa + iterável
    lambda produto: produto['preco'] >= 10,
    produtos
) 

print_iter(produtos)
print_iter(novos_produtos)