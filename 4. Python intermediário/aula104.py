# 'groupby': agrupando valores (itertools) (175)

from itertools import groupby

alunos = [
     {'nome': 'Luiz', 'nota': 'A'},
     {'nome': 'Letícia', 'nota': 'B'},

     {'nome': 'Gustavo', 'nota': 'A'},
     {'nome': 'Sofia', 'nota': 'C'},
     
     {'nome': 'Davi', 'nota': 'D'},
     {'nome': 'João', 'nota': 'A'},

     {'nome': 'Eduardo', 'nota': 'B'},
     {'nome': 'André', 'nota': 'A'},

     {'nome': 'Maria', 'nota': 'C'},
     {'nome': 'Gabriel', 'nota': 'A'}
]

# Os dados precisam estar ordenados para o 'groupby' agrupar corretamente

def ordenar_nota(alunos):
    return alunos['nota']

nota = sorted(alunos, key = ordenar_nota) # Iterável + função
grupo = groupby(nota, key = ordenar_nota)

for chave, valor in grupo:
    print(chave)

    for aluno in valor:
        print(aluno)