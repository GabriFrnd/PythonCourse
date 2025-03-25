# Funções decoradoras (165)
# Decoradores em Python (@syntax_sugar) (166)

'''
    Decorar: adicionar - remover - restringir - alterar
    Funções que decoram outras funções

    Decorador é uma função que recebe outra função como entrada, modifica ou adiciona algo a ela e a retorna
    O 'sytax_sugar' é uma maneira de melhorar a legibilidade e a expressividade do código
'''

def create_function(function): # Função decoradora

    def intern_function(*args, **kwargs):
        for arg in args:
            is_string(arg)

        result = function(*args, **kwargs)
        print('A função foi decorada!')

        return result

    return intern_function

@create_function # Indica que quero usar 'create_function' em 'inverter_string'
# Com '@create_function', o Python substitui automaticamente 'inverter_string' pela versão decorada que 'create_function' retorna

def inverter_string(string): # 'create_function' está decorando 'inverter_string'
    print(f'{inverter_string.__name__}') # 'inverter_string' virou 'intern_function'
    return string[::-1]

def is_string(parameter):
    if not isinstance(parameter, str):
        raise TypeError('O parâmetro deve ser uma string')
    
# O código comentado abaixo não tem 'syntax_sugar'

'''
string_invertida = create_function(inverter_string)
invertida = string_invertida(123)

print(invertida)
'''

# O código abaixo tem 'syntax_sugar'

invertida = inverter_string('Gabriel')
print(invertida)