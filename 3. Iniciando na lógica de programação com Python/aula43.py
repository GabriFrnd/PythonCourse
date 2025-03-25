# Tipo tuple (tuplas)
# Tuple é uma lista imutável

nomes = 'Maria', 'Helena', 'Luiz' # Tupla pode ser declarada como lista, mas sem [] ou com ()
frutas = ('Banana', 'Morango', 'Abacaxi') # Outra maneira de declarar uma tupla

print(nomes, type(nomes))
print(frutas, type(frutas))

lista = [123, True, 'Qualquer coisa']
tupla = tuple(lista) # Convertendo uma lista para uma tupla

print(tupla, type(tupla))