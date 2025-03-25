# While + while (laços internos)

colunas = 5
linhas = 5

linha = 1
while linha <= linhas:
    coluna = 1

    while coluna <= colunas:
        print(linha, coluna)
        coluna += 1

    linha += 1

print('Acabou.')