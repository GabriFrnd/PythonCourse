# Introdução às generator functions em Python

'''
Anotações da aula:

    - Generator function: função que sabe 'pausar'.
    - Toda generator function utiliza a palavra 'yield'.
'''

def generator(number): # Toda generator é um iterator.
    yield 1 # Virou 'return' e retorna 1; yield pausa a execução da função

    print('Continuando ...')
    yield 2 # Outra pausa

    return 'Fim da função.' # Levanta um 'StopIteration'

funcao_geradora = generator(0)

'''
print(next(funcao_geradora)) 
print(next(funcao_geradora))
print(next(funcao_geradora)) # Erro por falta de outro yield
'''

'''
for number in funcao_geradora: # Forma dinâmica
    # print(number)
'''

def numeros(number, max):
    while True:
        yield number # Pausa e retorna o valor atual

        if number >= max:
            return 'Fim.'
        
        number += 1

resultado = numeros(0, 10)

for number in resultado:
    print(number)