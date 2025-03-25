# Exercício: funções

def multiplicacao(multiplicador):
    def multiplicar(numero):
        return f'Resultado: {numero * multiplicador}'
    
    return multiplicar

duplicar = multiplicacao(2)
print(duplicar(10))

triplicar = multiplicacao(3)
print(triplicar(10))

quadruplicar = multiplicacao(4)
print(quadruplicar(10))