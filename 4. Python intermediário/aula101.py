# Exercício: somando duas listas (171)

primeira = [10, 20, 30, 40, 50]
segunda = [10, 20, 30]

# print(list(zip(primeira, segunda)))

resultado = [primeiro + segundo for primeiro, segundo in list(zip(primeira, segunda))]
print(resultado)