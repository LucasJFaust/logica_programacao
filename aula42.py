frase = ' O Python é uma liguagem de programação multiparadigma.' \
'Python foi criado por Guido van Rossum'

# Queremos saber qual letra apareceu mais vezes nas frases

i = 0 # Criando um índice
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

# Cada vez o while faz um loop, chamamos de iteração
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1

    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_atual = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi: "{letra_apareceu_mais_vezes}", {qtd_apareceu_mais_vezes} ')