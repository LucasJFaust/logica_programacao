"""
Fatiamento de strings
012345678
Olá Mundo
-987654321
Fatiamnto [i:f:p] [::]
OBS: a função len retorna a qtd de caracteres da string

"""

variavel = 'Olá mundo'

print(variavel[4:])
print(variavel[0:5])
print(variavel[-8:-2])
print(len(variavel[3]))
print(len(variavel[0:4]))
print(len(variavel))
print(variavel[0:len(variavel):1])
print(variavel[0:9:1])
print(variavel[0:9:2])
print(variavel[::-1])
print(variavel[-1:-10:-1])
