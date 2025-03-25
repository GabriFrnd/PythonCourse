# While: qual letra apareceu mais vezes na frase?

frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.'
index = 0

mais_vezes = 0 # Armazena quantas vezes uma determinada letra apareceu
letra_frequente = '' # Armazena a letra que mais apareceu

while index < len(frase):
    letra_atual = frase[index] # Captura cada letra da frase

    if letra_atual == ' ': # Condição que pula espaços na frase
        index += 1
        continue

    frequencia_letra = frase.count(letra_atual) # Registra quantas vezes cada letra apareceu

    if mais_vezes <= frequencia_letra:
        mais_vezes = frequencia_letra # Armazena a quantidade de vezes que a letra com maior frequência apareceu
        letra_frequente = letra_atual # Armazena a letra que apareceu mais vezes

    index += 1

print(f'Letra mais frequente: "{letra_frequente.upper()}" ({mais_vezes})')