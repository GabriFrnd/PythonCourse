# Try, except, else e finally + Built-in Exceptions
# Built-in Exceptions: https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    divisao = 10/0

except ZeroDivisionError as error:
    print(f'Erro: divisão por zero ({error.__class__.__name__}).')
    print(f'Mensagem: {error}.')

else: # Bloco executado quando não há erros
    print('Não há erros.')

finally: # Sempre será executado, mesmo com ocorrência de erros anteriormente
    print('Bloco do finally.')