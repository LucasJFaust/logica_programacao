"""
Interpolação Básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDF123456789)

"""
nome = 'Lucas'
preco = 1000.95897854
# variavel = 'Lucas, o preço total foi R$1000.95' Como podemos fazer isso por interpolação?
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))