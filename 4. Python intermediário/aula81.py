# Dictionary comprehension e set comprehension

produto = {
    'nome': 'caneta azul',
    'preco': 2.50,
    'categoria': 'escritório'
}

for chave, valor in produto.items():
    ...
    # print(f'{chave}: {valor}')

dictionary_comprehension = {
    chave: valor
    for chave, valor in produto.items()
}

print(dictionary_comprehension)

set_comprehension = {number for number in range(10)}
print(set_comprehension)