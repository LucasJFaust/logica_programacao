"""
Introdução ao desempacotamento + tuples (tuplas)
"""

# nome1, nome2, nome3 = ['Lucas', 'Pedro', 'Simone']
# print(nome2)

# nome1, *resto = ['Lucas', 'Pedro', 'Simone']  # Aqui estamos empacotando os outros dois valores
# print(nome1, resto)

_, _, nome2, *resto = ['Lucas', 'Pedro', 'Simone']  # Aqui estamos empacotando os outros dois valores
print(nome2, resto)
