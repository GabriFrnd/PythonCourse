# Listas dentro de listas (iteráveis dentro de iteráveis)

salas = [
    ['Maria', 'Helena'],
    ['Gabriel'],
    ['Luiz', 'João', 'Rafael']
]

# print(salas)
# print(salas[1][0]) # Gabriel

for sala in salas:
    print(f'Sala: {sala}')
    for aluno in sala:
        print(aluno)