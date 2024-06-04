"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
"""
import decimal

# n_1 = 0.1
# n_2 = 0.7
n_1 = decimal.Decimal(0.1)
n_2 = decimal.Decimal(0.7)
n_3 = n_1 + n_2
print(n_3)
print(f'{n_3:.2f}')
print(round(n_3, 3))