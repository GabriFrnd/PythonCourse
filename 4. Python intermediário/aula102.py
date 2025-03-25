# 'count' é um iterador sem fim (itertools) (173)

from itertools import count

contador = count() # Não tem fim
numeros = range(100) # Tem fim

print(f'{contador}, {hasattr(contador, '__iter__')}') # 'count' é um iterável
print(f'{contador}, {hasattr(contador, '__next__')}') # 'count' é um iterator

print(f'Range, {hasattr(numeros, '__iter__')}') # 'range' é um iterável
print(f'Range, {hasattr(numeros, '__next__')}') # 'range' não é um iterator

# print(next(contador))
# print(next(contador))

print()
print('Contador c/ count: ')

for numero in contador:
    if numero >= 100:
        break

    print(numero)

print()
print('Contador c/ range: ')

for numero in numeros:
    print(numero)