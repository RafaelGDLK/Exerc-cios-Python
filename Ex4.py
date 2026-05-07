# 4. Em um determinado momento em um jogo, é
# necessário calcular a medida da área de uma
# região por onde o jogador não poderá passar.
# Essa região é um triângulo e a medida da área é calculada a partir da fórmula ஻ . ு
# ଶ
# , sendo que B é a medida da base e H é a medida da altura desse triângulo.
# Crie um programa que mostre qual a área da
# figura a partir das medidas da base e da altura.

base = float(input('Qual a base do triângulo? '))
altura = float(input('Qual a altura do triângulo? '))

area = (base * altura) / 2

print('O resultado da área é', area)
