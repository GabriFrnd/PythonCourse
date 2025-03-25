# Exercício: funções

def multiplicacao(*args):
    total = 1

    for numero in args:
        total *= numero

    return total

resultado = multiplicacao(1, 2, 3, 4, 5)
print(f'Multiplicação: {resultado}')

def identidade(numero):
    if numero % 2 == 0:
        return f'O número {numero} é par.'
    
    return f'O número {numero} é ímpar.'

print(identidade(10))