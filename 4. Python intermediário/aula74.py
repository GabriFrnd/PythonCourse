# Introdução à função lambda + list.sort e sorted

'''
Anotações da aula:

    - Função lambda: função anônima que contém apenas uma linha.
    - 'sorted' cria uma nova lista ordenada, mas como shallow copy.
'''

'''
lista = [0, 20, 10, 50, 15, 25, 100]

lista.sort() # Ordena a lista em forma crescente
lista.sort(reverse=True) # Ordena a lista em forma decrescente
'''

lista = [
    {'nome': 'Gabriel', 'sobrenome': 'Fernandes Feitosa'},
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
]

'''
def ordenar(item):
    return item['nome'] # Ordena a lista pelo nome
'''
    
lista.sort(key=lambda item: item['nome']) # 'lambda' + parâmetro + retorno da função

for item in lista:
    print(item)