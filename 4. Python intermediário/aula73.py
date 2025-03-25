# Exercício: encontre o primeiro duplicado considerando a segunda ocorrência

lista_inteiros = [
    [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    [90, 10, 80, 90, 90, 70, 20, 10, 60, 80],

    [10, 30, 20, 20, 80, 60, 50, 90, 60, 70],
    [30, 80, 20, 80, 60, 70, 70, 30, 10, 90],

    [40, 80, 80, 80, 50, 10, 100, 30, 10, 70],
    [10, 30, 70, 20, 20, 10, 50, 10, 90, 90]
]

def encontrar_duplicado(lista_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1 # Flag

    for numero in lista_inteiros:

        if numero in numeros_checados:
            primeiro_duplicado = numero # Número (duplicado) com segunda ocorrência
            break

        numeros_checados.add(numero)

    return primeiro_duplicado

for lista in lista_inteiros:
    print(lista, encontrar_duplicado(lista))