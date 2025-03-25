# Como o for funciona por baixo dos panos? (next, iter, iterável e iterador)

'''
Iterável: str, range, etc (__iter__)
Iterador: quem sabe entregar um valor por vez

Next: me entregue o próximo valor
Iter: me entregue seu iterador
'''

texto = 'Gabriel' # Iterável
iterador = iter(texto) # Iterador

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break