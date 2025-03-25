# Exercício: sistema de perguntas e respostas

perguntas = [
    {
        'pergunta': 'Quanto é 2 + 2?',
        'opcoes': ['1', '3', '4', '5'],
        'resposta': '4'
    },
    {
        'pergunta': 'Quanto é 5 * 5?',
        'opcoes': ['25', '50', '10', '100'],
        'resposta': '25',
    },
    {
        'pergunta': 'Quanto é 10/2?',
        'opcoes': ['0', '10', '3', '5'],
        'resposta': '5'
    }
]

quantidade_acertos = 0

for pergunta in perguntas:
    print(f'Pergunta: {pergunta['pergunta']}')
    print()

    opcoes = pergunta['opcoes']

    for index, opcao in enumerate(opcoes):
        print(f'{index}) {opcao}')
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    quantidade_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < quantidade_opcoes:
            if opcoes[escolha_int] == pergunta['resposta']:
                acertou = True

    if acertou:
        print('Resposta certa!')
        quantidade_acertos += 1
    else:
        print('Resposta incorreta.')

    print()

print(f'Você acertou {quantidade_acertos} perguntas!')