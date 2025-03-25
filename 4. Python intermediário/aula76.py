# Empacotamento e desempacotamento de dicionários + *args e **kwargs

'''
Anotações da aula:

    - Kwargs: keyword arguments (argumentos nomeados).
'''

primeiro, segundo = 10, 20
primeiro, segundo = segundo, primeiro

# print(primeiro, segundo)

pessoa = {
    'nome': 'Gabriel',
    'sobrenome': 'Fernandes Feitosa'
}

dados_pessoa = {
    'idade': 20,
    'altura': 1.70
}

'''
primeira_chave, segunda_chave = pessoa # 'pessoa.values()' para pegar somente os valores
print(primeira_chave, segunda_chave)

for valor in pessoa.items():
    print(valor)

for chave, valor in pessoa.items():
    print(chave, valor) # Chave + valor fora de tuplas
'''

pessoa_completa = {**pessoa, **dados_pessoa} # Extração de chaves + valores dos dicionários (dois asteriscos)
# print(pessoa_completa)

def argumentos_nomeados(*args, **kwargs): # 'kwargs' sempre com dois asteriscos
    print(f'Argumentos não nomeados: {args}')
    print(f'Argumentos nomeados: {kwargs}')

argumentos_nomeados(10, 20, 30, nome = 'Gabriel', sobrenome = 'Fernandes Feitosa')