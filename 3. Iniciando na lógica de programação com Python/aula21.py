# Exercícios: enunciados

# Exercício I:

numero = input('Digite um número inteiro: ')
inteiro = ''

try:
    inteiro = int(numero)

    if inteiro % 2 == 0:
        print(f'O número digitado ({inteiro}) é par.')
    else:
        print(f'O número digitado ({inteiro}) é ímpar.')
except:
    print('O número digitado não é inteiro.')

# Exercício II:

horario = input('Digite o horário: ')
horario_inteiro = ''

try:
    horario_inteiro = int(horario)

    if horario_inteiro >= 0 and horario_inteiro <= 11:
        print('Bom dia!')
    elif horario_inteiro >= 12 and horario_inteiro <= 17:
        print('Boa tarde!')
    elif horario_inteiro >= 18 and horario_inteiro <= 23:
        print('Boa noite!')
    else:
        print('Erro.')
except:
    print('Algo deu errado.')

# Exercício III:

nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome)

try:
    tamanho = int(tamanho_nome)

    if tamanho <= 4:
        print('Seu nome é curto.')
    elif tamanho >= 5 and tamanho <= 6:
        print('Seu nome é normal.')
    elif tamanho > 6:
        print('Seu nome é muito grande.')
    else:
        print('Erro.')
except:
    print('Algo deu errado.')