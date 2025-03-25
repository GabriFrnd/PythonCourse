# Funções de primeira classe (higher order functions)

'''
Anotações da aula:

    - Higher order functions: funções que podem receber e/ou retornar outras funções.
    - First-class functions: funções que são tratadas como outros tipos de dados comuns.
'''

def cumprimento(mensagem, nome):
    return f'{mensagem}, {nome}!'

def funcao_executora(function, *args): # Higher order function
    return function(*args) # Retorna uma função com argumentos

print(funcao_executora(cumprimento, 'Bom dia', 'Gabriel'))