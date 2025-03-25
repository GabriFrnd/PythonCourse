# Concatenando e estendendo listas em Python

'''
Métodos úteis:

    - append: adiciona um item ao final da lista
    - insert: adiciona um item no índice escolhido

    - pop: remove um item do final ou do índice escolhido
    - del: apaga um índice

    - clear: limpa a lista
    - extend: estende a lista (não retorna nada)
'''

primeira_lista = [10, 20, 30]
segunda_lista = [40, 50, 60]

resultado = primeira_lista + segunda_lista
print(f'Junção das listas com "+": {resultado}')

primeira_lista.extend(segunda_lista) # Unindo a segunda lista à primeira
print(f'Primeira lista após o método "extend": {primeira_lista}')