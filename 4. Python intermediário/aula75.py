# Funções lambda complexas (para entendimento)

def executa(function, *args):
    return function(*args)

'''
def soma(primeiro_valor, segundo_valor):
    return f'Soma: {primeiro_valor + segundo_valor}'

def cria_multiplicador(multiplicador):
    def multiplicar(numero):
        return f'Resultado: {numero * multiplicador}'
    return multiplicar
'''

print(executa(lambda primeiro_valor, segundo_valor: f'Soma: {primeiro_valor + segundo_valor}', 10, 10)) # Função 'soma'

duplica = executa(lambda multiplicador: lambda numero: f'Resultado: {numero * multiplicador}', 10) # Função 'cria_multiplicador'
print(duplica(10)) # Parâmetro da função 'multiplicar'