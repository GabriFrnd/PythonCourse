# Métodos úteis do tipo 'set'

'''
Anotações da aula:

    - O método 'add' aceita apenas um valor por vez.
    - O método 'update', por outro lado, aceita mais de um valor por vez.
'''

conjunto = set()

conjunto.add('Gabriel') # Adiciona um valor no conjunto
print(conjunto)

conjunto.update(('Olá, mundo!', 10, 20, 30)) # Atualiza o conjunto com novos valores
print(conjunto)

conjunto.discard('Olá, mundo!') # Remove valores do conjunto
print(conjunto)

conjunto.clear() # Limpa o conjunto
print(conjunto)