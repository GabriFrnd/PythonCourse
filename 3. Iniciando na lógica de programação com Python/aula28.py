# While e else: recurso peculiar do Python

# O else é executado apenas quando o loop while finaliza naturalmente
# Caso haja um break, o else não será executado

string = 'Gabriel'
indice = 0

while indice < len(string):
    letra = string[indice]

    print(letra)
    indice += 1
else:
    print('O else foi executado.')

print('Fora do while.')