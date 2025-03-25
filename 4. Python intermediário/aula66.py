# Métodos úteis nos dicionários em Python

'''
Anotações da aula:

    1. len: número de chaves;
    2. keys: iterável com chaves;

    3. values: iterável com os valores;
    4. items: iterável com chaves e valores;

    5. setdefault: adiciona valor se a chave não existe;
    6. copy: retorna uma cópia rasa (shallow copy); # Aula 67

    7. get: obtém uma chave;
    8. pop: apaga um item com a chave especificada (del);

    9. popitem: apaga o último item adicionado;
    10. update: atualiza um dicionário com outro.
'''

pessoa = {
    'nome': 'Gabriel',
    'sobrenome': 'Fernandes Feitosa'
}

print(f'Número de chaves: {len(pessoa)}') # print(pessoa.__len__())
print(f'Chaves: {pessoa.keys()}')

for chave in pessoa.keys(): # 'chave in pessoa'
    ...
    # print(chave)

print(f'Valores: {pessoa.values()}')

for valor in pessoa.values():
    ...
    # print(valor)

print(f'Chaves e valores: {pessoa.items()}')

for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')

carro = {
    'marca': 'Porsche',
    'modelo': 911
}

carro.setdefault('ano', 2025) # Valor padrão (2025) para a chave 'ano' que não está no dicionário

print(carro)
print(f'Chave com get: {carro.get('marca')}') # Caso a chave 'marca' não exista, retornará 'None'

marca = carro.pop('marca') # Exclusão da chave 'marca'
print(f'Chave deletada: {marca}, Dicionário atual: {carro}')

ultima_chave = carro.popitem() # Elimina a última chave adicionada (ano)
print(f'Chave deletada: {ultima_chave}, Dicionário atual: {carro}')

outra_pessoa = {
    'nome': 'Rafael',
    'sobrenome': 'Fernandes Feitosa'
}

print(outra_pessoa)

outra_pessoa.update({ # outra_pessoa.update(nome = 'outro valor', idade = 30)
    'nome': 'outro valor',
    'idade': 30 # Pode-se adicionar também novas chaves e valores
})

print(outra_pessoa)