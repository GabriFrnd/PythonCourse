# Tipo list: introdução às listas mutáveis em Python

'''
Tipo list (array do JavaScript): mutável
Suporta vários valores de qualquer tipo
'''

lista = ['Livro', 123, 2.5, True, ['Outra lista']]

print(lista, type(lista))
print(lista[1], type(lista[1]))

lista[3] = False # Alterando o valor 'True' para 'False' na lista
print(lista)