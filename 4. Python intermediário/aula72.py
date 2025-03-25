# Operadores importantes para o tipo 'set'

'''
Anotações da aula:

    - Operadores úteis:

        1. União (|): une;
        2. Intersecção (&): itens presentes em ambos;

        3. Diferença (-): itens presentes apenas no conjunto da esquerda;
        4. Diferença simétrica (^): itens que não estão em ambos.
'''

primeiro_conjunto = {10, 20, 30}
segundo_conjunto = {20, 30, 40}

uniao = primeiro_conjunto | segundo_conjunto
print(f'União: {uniao}')

interseccao = primeiro_conjunto & segundo_conjunto
print(f'Intersecção: {interseccao}')

diferenca = primeiro_conjunto - segundo_conjunto # Conjunto da esquerda: 'primeiro_conjunto'
print(f'Diferença: {diferenca}')

diferenca_simetrica = primeiro_conjunto ^ segundo_conjunto
print(f'Diferença simétrica: {diferenca_simetrica}')