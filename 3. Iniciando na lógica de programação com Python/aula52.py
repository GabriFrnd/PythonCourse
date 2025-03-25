# Exercício: gerar dígitos de um CPF

'''
Rascunho de contas (100.359.730-05):
Conta para o primeiro dígito:

    Resultado da soma: 10 + 21 + 30 + 45 + 28 + 9 = 143
    Multiplicação: 143 * 10 = 1430
    Resto: 1430 % 11 = 0

Conta para o segundo dígito:

    Resultado da soma: 11 + 24 + 35 + 54 + 35 + 12 = 171
    Multiplicação: 171 * 10 = 1710
    Resto: 1710 % 11 = 5
'''

import re # Regular expressions
import sys

# Primeiro dígito:

entrada = input('Digite um CPF: ')
cpf = re.sub(r'[^0-9]', '', entrada) # '100.359.730-05'.replace('.', '').replace('-', '')

entrada_sequencial = entrada == entrada[0] * len(entrada)

if entrada_sequencial:
    print('Incorreto. Dados sequenciais!')
    sys.exit()

nove_digitos = cpf[0:9]

primeiro_contador = 10
primeira_soma = 0

for digito in nove_digitos:
    primeira_soma += primeiro_contador * int(digito)
    primeiro_contador -= 1

primeiro_digito = (10 * primeira_soma) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

# Segundo dígito:

dez_digitos = cpf[0:10]
segundo_contador = 11
segunda_soma = 0

for digito in dez_digitos:
    segunda_soma += segundo_contador * int(digito)
    segundo_contador -= 1

segundo_digito = (segunda_soma * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

novo_cpf = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if novo_cpf == cpf:
    print(f'O CPF enviado ({cpf}) é válido.')
else:
    print(f'O CPF enviado ({cpf}) é inválido.')