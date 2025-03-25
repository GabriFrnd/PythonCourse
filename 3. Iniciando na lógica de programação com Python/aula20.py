# Flags, is, is not e None

condicao = True
variavel = None

if condicao:
    variavel = True
    print('Faça algo')
else:
    print('Não faça algo')

print(variavel, variavel is None)
print(variavel, variavel is not None)