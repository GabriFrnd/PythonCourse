# Raise: lançando exceções (erros)

'''
Anotações da aula:

    - O que vier abaixo de um 'raise' não será executado.
    - Sintaxe: raise + erro + (mensagem).
    - Em uma função, o erro deve ser tratado à parte (fora dela).
'''

def dividir_zero(divisor):    
    if divisor == 0:
        raise ZeroDivisionError('Erro: divisor igual a zero.')
    
    return True

def tipo_dado(numero):
    if not isinstance(numero, (float, int)):
        raise TypeError('Erro: tipo de dado inválido.')

    return True


def divisao(numero, divisor):
    '''
    try:
        return f'Divisão: {numero/divisor}'
    
    except ZeroDivisionError:
        print('Bloco do except.')
        raise # Re-lançando o erro (redundante)'
    '''

    dividir_zero(divisor)
    
    tipo_dado(numero)
    tipo_dado(divisor)
        
    return f'Divisão: {numero/divisor}'

print(divisao(10, 1))