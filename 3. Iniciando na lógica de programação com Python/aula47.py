# Split, join e strip: métodos úteis para strings

# O 'split' recebe como parâmetro onde a string será dividida
# O 'join' une strings

frase = 'Olha que coisa interessante!'
string = 'Olá, mundo!'

lista_palavras = frase.split() # Divide uma string (retorna uma lista)
grupo_palavras = string.split(',') # Divide a string na vírgula, que não será incluída

print(lista_palavras)
print(grupo_palavras)

for index, palavras in enumerate(grupo_palavras):
    print(grupo_palavras[index].strip()) # 'strip' remove os espaços