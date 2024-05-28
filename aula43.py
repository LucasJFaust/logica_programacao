# Aula FOR

# Não é uma boa prática utilizar while para se iterar de strings que conhecemos o tamnho
# texto = 'Python'
# i = 0
# tamanho_string = len(texto)

# while i < tamanho_string:
#     print(texto[i], i)

#     i += 1

# É mais comum usarmos while para iteraveis que não conhecemos o tamanho ou quando desconhecemos o número de repetições como: 

# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')

# No caso do for ele se itera de maneira muito mais simples. Só temos que criar uma váriavel temporária para ele usar.

# texto = 'Python'

# for letra in texto:
#     print(letra)

texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')
