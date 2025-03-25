# Enumerate para enumerar valores de iteráveis (pegar índices)

lista = ['Maria', 'Helena', 'Luiz']
lista_enumerada = enumerate(lista) # enumerate recebe um iterável

for item in lista_enumerada:
    print(item) # 'item' retornará uma tupla

'''
for index, valor in enumerate(lista):
    print(index, valor)
'''