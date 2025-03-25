# Problema dos parâmetros mutáveis em funções Python (191)

def adicionar_clientes(nome, lista = []):
    lista.append(nome)
    return lista

minha_lista = []

primeiro_cliente = adicionar_clientes('Gabriel', minha_lista)
adicionar_clientes('Sofia', primeiro_cliente)

segundo_cliente = adicionar_clientes('Maria')
adicionar_clientes('Davi', segundo_cliente)

print(f'Lista criada externamente: {primeiro_cliente}')
print(f'Lista da função: {segundo_cliente}')