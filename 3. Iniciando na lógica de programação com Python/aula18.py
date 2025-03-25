# Introdução ao try e except para capturar erros (exceptions)

numero = input('Digite um número: ')

try:
    novo_numero = int(numero)
    print(f'O dobro de {novo_numero} é {novo_numero * 2}')
except:
    print('Algo deu errado.')