# Imprecisão dos números de ponto flutuante + round e decimal.Decimal

import decimal

soma = 0.1 + 0.7
print(soma) # 0.7999 ...

# Formas para corrigir imprecisão de números:

print(f'{soma:.2f}') # 0.80
print(round(soma, 2)) # Recebe dois parâmetros: número para arredondar e quantidade de casas decimais para mostrar

primeiro = decimal.Decimal('0.1')
segundo = decimal.Decimal('0.7')

print(primeiro + segundo)