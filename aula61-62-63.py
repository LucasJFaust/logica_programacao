"""
Validação de CPF

Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
A soma dos 9 primeiros números é usada para gerar o primeiro digiro depois do "-", e o segundo digito leva em consideração os 9 números mais o primeiro dígito.

Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301

Multiplicar o resultado anterior por 10
301 * 10 = 3010

Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7

Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7, o que leva o primeiro dígito ser válido.
"""
# cpf = '746.824.890-70'.replace('.', '').replace(' ', '').replace('-', '')  # Aqui usamos o método replace para substituir os caracteres indesejados
cpf_enviado_usuario = '746.824.890-70'

# Podemos também fazer por expressão regular:
import re
import sys

entrada = input('CPF [746.824.890-70]: ')
cpf_enviado_usuario = re.sub(r'[^0-9]', '', entrada)  # Aqui estamos usando um médtodo e estamos dizendo que ele encontre todo que não é um número e substitua para '':

entrada_sequqencial = entrada == entrada[0] * len(entrada)

if entrada_sequqencial:
    print('Você enviou dados sequenciais')
    sys.exit()

# 1. Primeiro precismos pegar os 9 primeiros dígitos do cpf:
nove_digitos = cpf_enviado_usuario[:9]

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

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é valido!')
else:
    print('cpf inválido')