# While + continue: pulando repetições

contador = 0

while contador != 20:
    contador += 1

    if contador == 3:
        print('Não tem mais o número 3.')
        continue

    if contador == 10:
        print('Aqui tinha o número 10.')
        continue

    if contador >= 15 and contador <= 17:
        print('')
        continue

    print(contador)

print('Acabou.')