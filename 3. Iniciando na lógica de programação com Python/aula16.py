# Fatiamento de strings e a função 'len'

# Fatiamento: [início:fim:passo]
# O índice final não é incluído

variavel = 'Olá, mundo!'

print(len(variavel)) # Quantidade de caracteres da variável
print(variavel[0:3]) # print(variavel[:3])

print(variavel[5:11]) # print(variavel[5:])
print(variavel[:len(variavel):1]) # 'Olá, mundo!'

print(variavel[::-1]) # Inversão da variável ('!odnum ,álO')