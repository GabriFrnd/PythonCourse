# Introdução às funções em Python

'''
Anotações da aula:

    - Por padrão, funções em Python retornam None (nada).
    - Função: trecho de código usado para replicar determinada ação ao longo do código.
    - Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
'''

def funcao(): # Declaração: 'def' + nome da função + ():
    return 'Isso é uma função.'

print(funcao()) # Chamada da função

def soma(primeiro, segundo): # Parâmetros da função: 'primeiro' e 'segundo'
    return f'Soma: {int(primeiro) + int(segundo)}'

print(soma(10, 5)) # Argumentos da função: '10' (primeiro) e '5' (segundo)

def cumprimento(nome='Gabriel'): # Parâmetro + argumento
    return f'Olá, {nome}!'

print(cumprimento())