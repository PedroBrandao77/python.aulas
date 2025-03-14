# apagando a tela
import os
os.system("cls")

dinheiro = float(input("Digite a quantidade de dinheiro disponivel"))
paes = dinheiro / 1.14
print("Qual o total de paes que pode ser comprado? ", paes)
troco = dinheiro % 1.14
print("valor do troco", troco)
