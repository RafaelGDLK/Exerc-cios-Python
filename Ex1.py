# 1. Crie um programa que peça a maior nota que um
# jogo obteve, a menor nota que o jogo obteve, calcule e exiba a nota média
# do jogo.

maior = float(input("Qual foi a maior nota do jogo? "))
menor = float(input("Qual foi a menor nota do jogo? "))

media = (maior + menor) / 2

print(f"A média entre a maior e a menor nota é {media:.2f}")
