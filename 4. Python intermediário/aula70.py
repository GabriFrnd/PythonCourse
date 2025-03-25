# Peculiaridades do tipo 'set'

primeiro_conjunto = {10, 20, 30, 10, 10, 20}
print(primeiro_conjunto) # Remoção de valores duplicados

lista = [0, 10, 20, 0, 10, 20]

outro_conjunto = set(lista) # Convertendo 'list' para 'set'
nova_lista = list(outro_conjunto) # Convertendo 'set' para 'list'

print(outro_conjunto) # Conjunto sem valores duplicados
print(nova_lista) # Lista sem valores duplicados

for numero in primeiro_conjunto:
    print(numero) # Iteração com remoção de valores duplicados