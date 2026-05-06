# 2. Em um jogo de exploração, os jogadores
# recebem dinheiro do jogo conforme
# percorrem determinados caminhos, sendo
# que o jogador recebe D$ 2,5 por quilômetro
# percorrido.
# Crie um programa que permita saber qual
# será o valor que um jogador deverá receber no final de um caminho.

km_percorrido = float(input('Quantos quilômetros foram percorridos? '))

valor_final = km_percorrido * 2.5

print (f'O valor final a receber ápos os quilometros percorridos é {valor_final:.2f}')
