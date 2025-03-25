# Formatação de strings com o método 'format'

a = 'A'
b = 'B'
c = 1.1

string = 'Variável A: {} - Variável B: {} - Variável C: {:.2f}'
formato = string.format(a, b, c)

print(formato)