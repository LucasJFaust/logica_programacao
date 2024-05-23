# Exercicio: Cheque se um valor é maior que o outro. Caso o valor seja maior ele deve ser mostrado primeiro.

primeiro_valor: str = input('Digite um valor: ')
segundo_valor: str = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(f'O primeiro valor {primeiro_valor} é maior que o segundo valor {segundo_valor}')
elif segundo_valor >= primeiro_valor:
    print(f'O segundo valor {segundo_valor} é maior que o primeiro valor {primeiro_valor}')
