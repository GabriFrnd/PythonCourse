# Ordem de aplicação dos decoradores (168)

def parametros_decorador(nome):

    def decorador(function):
        print(f'Decorador: {nome}')

        def nova_funcao(*args, **kwargs):
            resultado = function(*args, **kwargs)
            final = f'{resultado}, {nome}'

            return final
        
        return nova_funcao
    return decorador

# Primeiro, executa-se o decorador mais perto da função (de baixo para cima)

@parametros_decorador(nome = 'terceiro')
@parametros_decorador(nome = 'segundo')
@parametros_decorador(nome = 'primeiro')

def soma(primeiro_valor, segundo_valor):
    return f'Soma: {primeiro_valor + segundo_valor}'

somar = soma(10, 10)
print(somar)