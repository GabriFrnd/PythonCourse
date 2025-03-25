# Mapeamento de dados em list comprehension (map)

'''
Anotações da aula:

    - Mapeamento: nova lista com, talvez, dados transformados, mas com o mesmo tamanho da lista original.
'''

produtos = [
    {'nome': 'Lápis', 'preco': 2.50},
    {'nome': 'Caneta', 'preco': 3.00},
    {'nome': 'Caderno', 'preco': 5.00}
]

novos_produtos = [produto for produto in produtos]
print(*novos_produtos)

nomes_produtos = [produto['nome'] for produto in produtos]
print(f'Nomes: {nomes_produtos}')

precos_produtos = [produto['preco'] for produto in produtos]
print(f'Preços: {precos_produtos}')

aumento_preco = [
    {**produto, 'preco': produto['preco'] - 1.00} 
    if produto['preco'] >= 5.00 else {**produto} # Diminui o preço do produto caso ele seja maior ou igual a R$ 5.00

    for produto in produtos
]

print(f'Aumento de preço: {aumento_preco}')