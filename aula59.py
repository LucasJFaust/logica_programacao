# Desempacotamento em chamadas de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
#..........0.........1
salas = [['Maria', 'Helena'], # 0
#...........0
         ['Elaine', ], # 1
#..........0.........1.......2
         ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)]] # 2

# p, b, *_, ap, u = lista
# print(p, u, ap)

# for nome in lista:
#     print(nome, end=' ')

# print(*lista) # Aqui ele o print está fazendo algo semelhante ao for e igual ao print de baixo
# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*string)
# print(*tupla)
print(*salas, sep='\n')