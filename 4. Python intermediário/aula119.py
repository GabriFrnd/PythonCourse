# Positional-Only Parameters (/) e Keyword-Only Arguments (*) (196)

'''
    '*args': ilimitado de argumentos posicionais
    '**kwargs': ilimitado de argumentos nomeados

    Positional-Only Parameters (/): tudo antes da barra deve ser apenas posicional
    Keyword-Only Arguments (*): '*' sozinho não suga valores

    Tudo que vem antes do asterico deve ser posicional
    Tudo que vem depois do asterisco deve ser nomeado
'''

def contas(primeiro, segundo, /, valor, outro_valor):
    print(f'Soma: {primeiro + segundo}')
    print(f'Subtração: {valor - outro_valor}')

def multiplicacao(primeiro, segundo, *, terceiro): 
    return f'Multiplicação: {primeiro * segundo * terceiro}'

contas(10, 10, valor = 50, outro_valor = 25)
print(multiplicacao(3, 5, terceiro = 10))