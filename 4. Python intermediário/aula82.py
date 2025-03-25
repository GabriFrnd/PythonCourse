# 'isinstance()' para saber se um objeto é de determinado tipo

'''
Anotações da aula:

    - 'isinstance()': item a ser verificado e tipo de dado ('isinstance(item, str)', por exemplo).
    - Ao usar 'isinstance()', pode-se passar mais de um tipo utilizando uma tupla.
'''

lista = ['ABC', 123, 2.5, {'nome': 'Gabriel'}, {0, 10, 20}, (30, 40, 50), [60, 70, 80]]

for item in lista:
    if isinstance(item, str): # Verifica quais itens na lista são 'string'
        print(f'String: {item}')

    elif isinstance(item, int): # Verifica quais itens na lista são 'int'
        print(f'Inteiro: {item}')

    elif isinstance(item, (dict, set)): # Verifica quais itens na lista são 'dict' ou 'set'
        print(f'Dict ou set: {item}')

    else: 
        print(f'Outro tipo: {item}')