# While e break (estrutura de repetição)

condicao = True

while condicao:
    nome = input('Digite seu nome: ')

    if nome:
        print(f'O seu nome é {nome}')
    else:
        break

print('Acabou.')