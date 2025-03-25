# Combinations, permutations e product (itertools) (174)

'''
    Combinação: ordem não importa (iterável + tamanho do grupo)
    Permutação: ordem importa
    Produto: ordem importa e recebe valores únicos
'''

from itertools import combinations, permutations, product

pessoas = ['João', 'Gabriel', 'Sofia', 'Letícia']

camisetas = [
    ['Preta', 'Branca', 'Azul', 'Cinza'],
    ['P', 'M', 'G', 'GG'],

    ['Masculino', 'Feminino', 'Unissex'],
    ['Algodão', 'Linho', 'Poliéster']
]

def iter_print(iterator):
    print(*list(iterator), sep='\n') 
    print()

iter_print(combinations(pessoas, 2)) # Combina 'pessoas' em grupos de 2 (ordem não importa)
iter_print(permutations(pessoas, 2)) # Permuta 'pessoas' em grupos de 2 (ordem importa)
iter_print(product(*camisetas)) # Ordem importa + valores únicos