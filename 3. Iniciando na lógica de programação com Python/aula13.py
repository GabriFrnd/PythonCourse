# Exercício de programação com if e comparação

primeiro = int(input('Digite um valor: '))
segundo = int(input('Digite outro valor: '))

if primeiro > segundo:
    print(f'O primeiro valor ({primeiro}) é maior que o segundo ({segundo}).')
elif primeiro == segundo:
    print(f'Os valores são iguais.')
elif primeiro < segundo:
    print(f'O primeiro valor ({primeiro}) é menor que o segundo ({segundo}).')
else:
    print('Erro.')