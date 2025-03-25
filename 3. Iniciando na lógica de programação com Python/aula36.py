# Alterando uma lista com índices, del, append e pop

# Ao utilizar o 'del', os índices de uma lista serão reorganizados
# O 'pop' também recebe índices para serem removidos

lista = [10, 20, 30]
print(lista)

lista[2] = 25 # Alterando um valor da lista
print(lista)

del lista[0] # Deletando o primeiro elemento da lista (10)
print(lista)

lista.append(100) # Adiciona elementos no final da lista
print(lista)

lista.pop() # Remove o último elemento da lista (100)
print(lista)

lista.pop(0) # Remove o elemento que corresponde ao índice 0 na lista (20)
print(lista)