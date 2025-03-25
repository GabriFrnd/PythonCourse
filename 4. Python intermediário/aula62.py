# Closure e funções que retornam outras funções

def cumprimento(mensagem): # 'mensagem' será lembrado
    def saudar(nome): # 'nome' será dinâmico
        return f'{mensagem}, {nome}!'
    
    return saudar # O Python salva os valores dos parâmetros

primeiro = cumprimento('Bom dia') # 'primeiro' é uma nova função
print(primeiro('Gabriel')) # Closure (fechamento)

'''
for nome in ['Jucelia', 'Luis', 'Rafael']:
    print(primeiro(nome))
'''