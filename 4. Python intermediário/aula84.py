# Generator expression, iterables e iterators em Python

'''
Anotações da aula:

    - Generator: função que pausa.
    - Ele não possui tamanho e índice.
'''

import sys

iterable = ['Eu', 'tenho', '__iter__']
iterator = iterable.__iter__() # Tem __iter__ e __next__

lista = [number for number in range(1000)] 
generator = (number for number in range(1000)) # Generator expression (tupla)

print(sys.getsizeof(lista)) # Tamanho (bites); mais espaço na memória
print(sys.getsizeof(generator)) # Ocupa menos espaço na memória