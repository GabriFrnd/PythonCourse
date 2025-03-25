# Argumentos nomeados e argumentos posicionais (não nomeados) em funções

'''
Anotações da aula:

    - Argumento nomeado: nome com sinal de igual.
    - Argumento não nomeado: recebe apenas o argumento (valor).
    - Não é ideal misturar argumentos nomeados com não nomeados.
'''

def soma(primeiro, segundo):
    return f'Soma: {primeiro + segundo}'

print(soma(10, 5)) # Argumentos posicionais (não nomeados)
print(soma(primeiro=20, segundo=15)) # Argumentos nomeados