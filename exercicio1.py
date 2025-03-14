# apagando a tela
import os
os.system("cls")

n1 = float(input("Digite o primeiro numero "))
n2 = float(input("Digite o segundo numero "))
med = (n1 + n2) / 2
print(f"Media = {med}")

dinheiro = float(input("Digite o quanto de dinheiro disponivel "))
paes = dinheiro / 1,14
print("Qual o total de paes que pode ser comprado ", paes)
