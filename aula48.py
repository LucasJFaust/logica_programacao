"""
Listas em Python
Tipo: list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamentos
Métodos úteis: append, insert, pop, clear, extend, +.
CRUD -> Creat, Read, Update e Delete
"""
#........+12345
#........-54321
string = 'ABCDE'  # 5 caracteres
# print(bool(lista))  # False

#.........0.....1......2......3....4
#........-5....-4......-3....-2..-1
# lista = [123, True, 'Lucas', 1.2, []]  # ' '
# lista[-3] = 'Maria'
# print(lista[2].upper(), type(lista[2]))
# numero = lista[0]
# print(numero)
# del lista[2] # Depois de deletarmos um elemento de uma lista o python reorganiza o índice
# Devido a essa reorganização dos índices, é interessante só trabalharmos com mudanças no final dela.

# lista.append(50)  # Valor adicionado no final da lista
# lista.pop()  # Remouve o último item da lista no momento
# lista.clear()  # Limpa a lista
# lista.insert(0, 5)   # Com o insert, colocamos primeiro o índice da lista e depois o novo item da lista

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)

lista_d = lista_a.copy()  # Cpoia a lista a
