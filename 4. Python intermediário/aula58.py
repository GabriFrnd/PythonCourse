# Retorno de valores das funções (return)

'''
Anotações da aula:

    - A palavra 'return' indica que a função retorna algo.
    - Não se pode fazer nada na função depois do 'return'.
'''

def soma(primeiro_valor, segundo_valor): # A função retorna 'None'
    print(f'Soma: {primeiro_valor + segundo_valor}')

primeiro = soma(10, 10)
segundo = soma(5, 5)

# print(primeiro + segundo) - Erro, pois 'primeiro' e 'segundo' são None

def outra_soma(primeiro_valor, segundo_valor): # Essa função retorna algo
    return primeiro_valor + segundo_valor
    print('Qualquer coisa.') # Isso não será executado

primeiro_numero = outra_soma(10, 10)
segundo_numero = outra_soma(5, 5)

print(primeiro_numero + segundo_numero) # Sem erros