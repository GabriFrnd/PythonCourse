# Exercício: jogo da palavra secreta

import os

palavra = 'livro'
letras_corretas = ''
tentativas = 0

while True:
    letra = input('Digite uma letra: ')
    tentativas += 1

    if len(letra) > 1: # Verifica se o usuário digitou apenas uma letra
        print('Digite apenas uma letra.')
        continue

    if letra in palavra: # Verifica se a letra digitada pelo usuário está na palavra secreta
        letras_corretas += letra # Armazena na variável 'letras_corretas' as letras que o usuário digitou que estão na palavra secreta

    palavra_formada = ''
    for letra_secreta in palavra: # Realiza uma iteração na palavra secreta

        if letra_secreta in letras_corretas: # Verifica se o usuário acertou alguma letra que está na palavra secreta
            palavra_formada += letra_secreta # Armazena, a cada loop, a palavra correta sendo formada de acordo com os acertos do usuário

        else: # Caso o usuário não acerte alguma letra da palavra secreta, serão exibidos asteriscos nas letras não acertadas
            palavra_formada += '*' # Coloca-se asteriscos na palavra sendo formada nas letras não acertadas pelo usuário

    print(f'Palavra: {palavra_formada}') # Exibe a palavra sendo formada de acordo com os palpites do usuário

    if palavra_formada == palavra: # Verifica se o usuário acertou a palavra secreta
        os.system('cls') # Realiza a limpeza do terminal

        print(f'Parabéns, você acertou a palavra secreta: {palavra}!')
        print(f'Você acertou a palavra secreta em {tentativas} tentativas.')

        letras_corretas = '' # Zera as letras acertadas da palavra secreta
        tentativas = 0 # Zera o número de tentativas

        print() # Dá espaço entre as frases