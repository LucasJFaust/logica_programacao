'''
split e join com list e str
split -> divide uma string
join -> une uma string
'''

frase = 'Olha só, que coisa interessante'
lista_frases = frase.split(', ')

for i,frase in enumerate(lista_frases):
    print(lista_frases[i].strip())  # Strip corta os espaços no começo e no fim para cortar o da direita rstrip e esquerda lstrip

frase_unidas = '-'.join(lista_frases)

print(lista_frases)