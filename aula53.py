"""
enumerate -> Enumera iteráveis (Índices)
"""

lista = ['Lucas', 'Jose', 'Maria']
lista.append('João')

# lista_enumerada = list(enumerate(lista))
# print(next(lista_enumerada))

# for item in lista_enumerada:
#     print(item)

# for item in enumerate(lista):
#      indice, nome = item
#      print(indice, nome)

for indice, nome in enumerate(lista):
     print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#      print('FOR da tupla:')
#      for valor in tupla_enumerada:
#           print(f'\t{valor}')