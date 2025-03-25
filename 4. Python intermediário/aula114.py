# Salvando dados Python em JSON com módulo 'json' (190)

'''
    'json.dump': serializa um objeto Python para o formato JSON e escreve essa saída em um arquivo
    Escreve diretamente em um arquivo, enquanto 'json.dumps' retorna o JSON como string (sem gravar em arquivo)

    'json.load': desserializa um JSON que está em um arquivo, convertendo-o em um objeto Python correspondente
    Lê o JSON diretamente de um arquivo, enquanto 'json.loads' lê uma string contendo JSON e a converte em um objeto Python
'''

import json

pessoa = {
    'nome': 'Gabriel',
    'sobrenome': 'Fernandes Feitosa',

    'altura': 1.7,
    'idade': 20,

    'enderecos': [
        {'rua': 123, 'numero': 21},
        {'rua': 456, 'numero': 26},
    ],
}

with open('aula114.json', 'w', encoding='utf-8') as arquivo:
    json.dump( # Objeto para converter em JSON + arquivo onde deseja-se gravar o JSON + formatação amigável + codificação ASCII
        pessoa, arquivo, indent = 4, ensure_ascii = False
    )

with open('aula114.json', 'r', encoding='utf-8') as arquivo: # Para usar 'json.load' precisa estar em modo leitura
    pessoa = json.load(arquivo) # Recebe o arquivo que contém o JSON 

print(type(pessoa), pessoa) # Novamente um dicionário (dict)