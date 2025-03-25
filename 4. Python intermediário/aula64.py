# Introdução ao 'dict' (dicionários em Python)

'''
Anotações da aula:

    - Dicionário (mutável) é uma estrutura de dados do tipo par de 'chave' e 'valor'.
    - Usa-se as chaves ou a classe 'dict' para criar dicionários.

    - Em um dicionário, as chaves podem ser consideradas como 'índice'.
    - Apenas tipos imutáveis (str, int, float, bool, ...) podem ser chaves.
'''

pessoa = {
    'nome': 'Gabriel',
    'sobrenome': 'Fernandes Feitosa'
}

print(pessoa, type(pessoa))
# print(f'Nome completo: {pessoa["nome"]} {pessoa["sobrenome"]}')

outra_pessoa = dict(nome = 'Rafael', sobrenome = 'Fernandes Feitosa') # Isso também é um dicionário
print(outra_pessoa, type(outra_pessoa))

carro = {
    'nome': 'Porsche 911',
    'cor': 'Branco',
    'proprietario': [
        {'nome': 'Gabriel', 'sobrenome': 'Fernandes Feitosa'},
        {'endereco': 'Quadra 2, conjunto 4, casa 5'}
    ]
}

for chave in carro:
    print(f'{chave}: {carro[chave]}')