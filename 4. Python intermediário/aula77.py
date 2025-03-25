# Introdução à list comprehension em Python

'''
Anotações da aula:

    - List comprehension: forma rápida para criar listas a partir de iteráveis.
    - À esquerda da palavra 'for' vai o que será incluído na lista.
'''

lista = [numero for numero in range(10)]

print(f'List comprehension: {lista}')
print(f'Print + range: {list(range(10))}') # Mesmo resultado

multiplicacao = [numero * 2 for numero in range(10)] # Cada número, de 0 a 9, será multiplicado por 2
print(f'Multiplicação: {multiplicacao}')