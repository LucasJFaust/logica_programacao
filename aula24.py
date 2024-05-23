# Operadores in (está entre) e not in (não está entre)
#Strings são iteráveis, ou seja, podemos navegar item por item no python apenas utilizando os indices da string
# 0 1 2 3 4
# L u c a s
# -4-3-2-1

# nome = 'Lucas'

# print(nome[2])
# print(nome[-2])

# print('f' in nome)
# print('f' not in nome)

nome = input('Digit o seu nome: ')
encontrar = input('Digite o que desejar encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')