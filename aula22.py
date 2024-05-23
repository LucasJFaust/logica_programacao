# or (ou): Qualquer condição verdadeira avalia toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro a expressão inteira será avaliada naquele valor.
# São considerados falsy 0, 0.0. '': False
# Também existe o tipo None que é usado para representar um não valor

# entrada: str = input('[E]ntrar [S]air: ')
# senha_digitada: str = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de Curto Circuito:
# senha = 0 or False or 0 or 'abc' or True
senha = input("Senha: ") or 'Sem senha'
print(senha)