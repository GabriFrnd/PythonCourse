# Decoradores com parâmetros (167)

def fabrica_decoradores(primeiro = None, segundo = None, terceiro = None): # Tem acesso a três escopos
    def fabrica_funcoes(function):
        print('Primeira decoradora')

        def funcao_aninhada(*args, **kwargs):
            print(f'Parâmetros do decorador: {primeiro, segundo, terceiro}')
            print('Função aninhada')

            resultado = function(*args, **kwargs)
            return resultado

        return funcao_aninhada
    return fabrica_funcoes

# @fabrica_funcoes 

# '@fabrica_funcoes' substitui 'soma' por 'funcao_aninhada'
# 'funcao_aninhada' só será executada quando 'soma' for executada

@fabrica_decoradores(10, 20, 30)

def soma(primeiro_valor, segundo_valor):
    return f'Soma: {primeiro_valor + segundo_valor}'

somar = soma(10, 10)
print(somar)

multiplicar = fabrica_decoradores()(lambda primeiro, segundo: f'Multiplicação: {primeiro * segundo}')
resultado = multiplicar(10, 10)

print(resultado)