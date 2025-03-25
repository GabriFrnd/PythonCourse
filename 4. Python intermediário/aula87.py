# Try e except para tratar exceções

try:
    primeiro_valor = 10
    segundo_valor = 0[10] # Erro
    divisao = primeiro_valor / segundo_valor

except ZeroDivisionError: # Exceção a ser tratada: divisão por zero
    print('Erro: divisão por zero.')

except NameError: # Exceção a ser tratada: variável não declarada
    print('Erro: variável não declarada.')

except (TypeError, IndexError) as error: # Pode-se tratar dois erros juntos com uma tupla
    print('Erro: TypeError e/ou IndexError.')
    print(f'Erro: {error} ({error.__class__.__name__})') # Mensagem direta de erro + classe do erro

except Exception: # Maior classe de erros; trata de qualquer erro
    print('Erro ocorrido.')

print('Fim do try/except.') # No 'except', indicar sempre a exceção a ser tratada.