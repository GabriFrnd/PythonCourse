# '*args' para quantidade de argumentos não nomeados variáveis

'''
Anotações da aula:

    - *args: empacotamento e desempacotamento
'''

primeiro, segundo, *resto = 1, 2, 3, 4, 5
# print(primeiro, segundo, resto)

def soma(*args): # '*args' é tudo o que for passado como argumento não nomeado para a função
    total = 0

    for numero in args:
        total += numero

    return total

    # return args, type(args)

print(soma(1, 2, 3, 4, 5))
print(sum((1, 2, 3, 4, 5))) # Realiza o mesmo que a função 'soma'