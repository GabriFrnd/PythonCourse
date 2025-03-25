# Desempacotamento em chamadas de funções

string = 'ABC'
tupla = 'Python', 'é', 'legal'
lista = ['Gabriel', 'Helena', True, 2.5, 123]

primeiro, segundo, *_, ultimo = lista
# print(primeiro, ultimo)

'''
for item in lista:
    print(item)
'''

# print(*string)
print(*lista, sep='\n') # Iterando pela lista
# print(*tupla)