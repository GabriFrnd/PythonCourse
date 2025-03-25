# Funções recursivas, recursividade e Stack Overflow (179)
# Limite de recursão e cuidados com funções recursivas (180)

'''
    Funções recursivas: funções que podem se chamar de volta
    Requisitos:

        Um problema que possa ser dividido em partes menores
        Caso recursivo que resolve o problema
        Um caso base que encerra a recursão
'''

import sys
sys.setrecursionlimit(1000) # Não recomendado!

'''
def funcao_recursiva(start = 0, stop = 10):    
    if start >= stop:
        return stop
    
    print(start, stop)

    start += 1
    return funcao_recursiva(start, stop)

print(funcao_recursiva(0, 1000))
'''

def funcao_fatorial(number):
    if number <= 1:
        return 1
    
    return number * funcao_fatorial(number - 1)

print(funcao_fatorial(5))
print(funcao_fatorial(10))