"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
....<- Contagem de complexidade (ruim)
"""
velocidade = 61 # Velocidade atual do carro
local_carro = 100 # local que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_1) and local_carro <= (LOCAL_1 + RADAR_1)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

# O Contratante quer saber se o carro passou da velocidade do radar 1
if vel_carro_pass_radar_1:
    print('Velocidade maior que radar 1')

if carro_passou_radar_1:
    print('Carro passou no radar 1')

if  carro_multado_radar_1:
    print('Carro multado em radar 1')