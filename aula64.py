# Vamos ver a variação do exercicío gerando os digitos de maneira aleatória:
import random
import sys

# 1. Imagine que eu queira um número aleatório entre 0 e 9 com 9 digitos:
for _ in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    # 2. Agora queremos fazer a multiplicação desses valores com um contador regressivo comaçando do 10 até o 2 e depois somar os valores:
    contador_regressivo_01 = 10

    resultado_01 = 0
    for digito in nove_digitos:
        resultado_01 += int(digito) * contador_regressivo_01
        contador_regressivo_01 -= 1

    # 3. Agora vamos multiplicar o resultado por 10 e pegar o resto da divisão por 11:
    digito_01 = (resultado_01 * 10) % 11

    # 4. Agora vamos atender a condicional usando o ternário:
    digito_01 = digito_01 if digito_01 <= 9 else 0
    print(digito_01)

    # 5. Agora vamos atuar no segundo digito seguindo a mesma lógica:
    daz_digitos = nove_digitos + str(digito_01)

    contador_regressivo_02 = 11

    resultado_02 = 0
    for digito in daz_digitos:
        resultado_02 += int(digito) * contador_regressivo_02
        contador_regressivo_02 -= 1

    digito_02 = (resultado_02 * 10) % 11

    digito_02 = digito_02 if digito_02 <= 9 else 0
    print(digito_02)

    # 6. Agora vamos validar o cpf

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_01}{digito_02}'

    print(cpf_gerado_pelo_calculo)