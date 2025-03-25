# Manipulando chaves e valores em dicionários

pessoa = {}

pessoa['nome'] = 'Gabriel' # Criando um par de chave-valor no dicionário 'pessoa'
pessoa['sobrenome'] = 'Fernandes Feitosa'

chave = 'idade' # Chave dinâmica
pessoa[chave] = 20

pessoa['altura'] = 1.70
print(pessoa)

del pessoa['altura'] # Apagando a chave 'altura' do dicionário
print(pessoa)