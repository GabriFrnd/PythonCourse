# Valores-padrão para parâmetros em funções + NoneType e None

'''
Anotações a aula:

    - Ao definir uma função, os parâmetros podem ter valores-padrão.
    - Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.
    - Todo parâmetro que vier depois de um com valor padrão também precisará ter um valor padrão.
'''

def soma(primeiro, segundo, terceiro = 5): # 'terceiro' tem um valor padrão
    if terceiro is not None:
        return f'Soma: {primeiro + segundo + terceiro}'
    else:
        return f'Soma: {primeiro + segundo}'

print(soma(10, 10)) # Não será necessário passar o valor de 'terceiro'