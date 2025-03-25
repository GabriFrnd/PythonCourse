# Variáveis livres + nonlocal (locals, globals)

''' print(globals()) # Exibe todas as variáveis globais que estão definidas '''

def funcao_fora(valor):
    variavel = valor # Não está definida dentro do escopo de 'funcao_dentro' (variável livre)

    def funcao_dentro():
        print(locals()) # Exibe quais variáveis são locais
        return variavel
    
    return funcao_dentro

primeiro_dentro = funcao_fora(10)
segundo_dentro = funcao_fora(20)

'''
print(primeiro_dentro())
print(segundo_dentro())
'''

def concatenar(string_inicial):
    valor_final = string_inicial

    def funcao_interna(valor_concatenar):
        nonlocal valor_final # Indica para o Python que 'valor_final' não é uma variável local
        valor_final += valor_concatenar
        
        return valor_final
    
    return funcao_interna

resultado = concatenar('A')

print(resultado('B'))
print(resultado('C'))