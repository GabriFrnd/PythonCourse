# 'yield from' em generator functions

def first_generator():
    yield 1
    yield 2
    yield 3

def second_generator():
    yield from first_generator() # Continuação do 'first_generator'
    yield 4

    yield 5
    yield 6

gen = second_generator()

for numbers in gen:
    print(numbers)