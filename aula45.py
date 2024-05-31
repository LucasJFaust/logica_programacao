"""
Como o For funciona por baixo dos panos:
Interável -> str, range, etc (Ele tem um método dentro dele chamado __iter__ que é uma ação que chamamos dentro do meu objeto com o ".")
Iterador -> quem sabe entragar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
texto = iter('Lucas')  # __iter__()
iterador = iter(texto)

# while True:
#     try:
#         letra = (next(iterador))
#         print(letra)
#     except StopIteration:
#         break

numeros = range (0, 100, 8)

for numero in numeros:
    print(numero)