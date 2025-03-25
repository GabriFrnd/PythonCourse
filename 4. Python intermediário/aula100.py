# Exercício: unir listas + zip e zip_longest do itertools (169 e 170)

from itertools import zip_longest

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
siglas = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(cidades, siglas))) # Utiliza o valor da lista menor

def zipper(primeira, segunda):
    intervalo = min(len(primeira), len(segunda)) # Busca o menor tamanho entre as listas
    return [(primeira[index], segunda[index]) for index in range(intervalo)]

print(zipper(cidades, siglas))
print(list(zip_longest(cidades, siglas, fillvalue='Sem cidade'))) # Utiliza o valor da lista maior