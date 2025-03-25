# Exercício: adiando execução de funções (162)

def somar(primeiro, segundo):
    return f'Soma: {primeiro + segundo}'

def multiplicar(primeiro, segundo):
    return f'Multiplicação: {primeiro * segundo}'

def criar_funcao(function, primeiro):
    def funcao_interna(segundo):
        return function(primeiro, segundo)
    
    return funcao_interna

somar_cinco = criar_funcao(somar, 5)
multiplicar_dez = criar_funcao(multiplicar, 10)

print(somar_cinco(5))
print(multiplicar_dez(10))