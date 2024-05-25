"""
Inteirando
"""
#       0123456789
nome = 'Lucas José Faust' # Iteráveis

tamanho_nome = len(nome)

indice = 0
novo_nome = ''
# while indice < len(nome):
#     print(nome[indice])
#     indice += 1

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)