# Criando um gerador de CPFs

import random

for _ in range(100):
    nove_digitos = ''

    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    primeiro_contador = 10
    primeira_soma = 0

    for digito in nove_digitos:
        primeira_soma += primeiro_contador * int(digito)
        primeiro_contador -= 1

    primeiro_digito = (10 * primeira_soma) % 11
    primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

    dez_digitos = nove_digitos + str(primeiro_digito)
    segundo_contador = 11
    segunda_soma = 0

    for digito in dez_digitos:
        segunda_soma += segundo_contador * int(digito)
        segundo_contador -= 1

    segundo_digito = (segunda_soma * 10) % 11
    segundo_digito = segundo_digito if segundo_digito <= 9 else 0

    novo_cpf = f'{nove_digitos}{primeiro_digito}{segundo_digito}'
    print(novo_cpf)