# Calculadora (exercício guiado)

while True:
    primeiro = input('Digite um número: ')
    segundo = input('Digite outro número: ')

    operador = input('Digite um operador (+ - * /): ')
    numeros_validos = None

    primeiro_numero = 0
    segundo_numero = 0

    try:
        primeiro_numero = float(primeiro)
        segundo_numero = float(segundo)
        
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Digite apenas números válidos.')
        continue

    operadores_validos = '+-*/'

    if operador not in operadores_validos:
        print('Operador válido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '+':
        print(f'Resultado: {primeiro_numero + segundo_numero}')
    elif operador == '-':
        print(f'Resultado: {primeiro_numero - segundo_numero}')
    elif operador == '*':
        print(f'Resultado: {primeiro_numero * segundo_numero}')
    elif operador == '/':
        print(f'Resultado: {primeiro_numero / segundo_numero}')
    else:
        print('Erro.')

    sair = input('Deseja sair? ').lower().startswith('s')

    if sair:
        break