# List comprehension com mais de um 'for'

'''
Anotações da aula:
'''

nova_lista = []

for primeiro in range(3):
    for segundo in range(3):
        nova_lista.append((primeiro, segundo))

print(nova_lista)

outra_lista = [
    (primeiro, segundo) for primeiro in range(3) # Primeiro 'for' com valores à esquerda
    for segundo in range(3) # Segundo 'for' sem valor à esquerda (segundo valor junto com o primeiro)
]

print(outra_lista)