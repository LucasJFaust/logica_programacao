"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop Infinito -> Quando um código não tem fim
"""
# contador = 0

# while contador <= 10:
#     contador += 1
#     print(contador)

#     if contador == 4:
#         break

# print('Acabou')

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Usei o continue para não mostrar o 6')
        continue

    if contador >= 10 and contador <=27:
        print('Estou pulando o', contador)
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou')