#Principais formatações : 5 e 8
 
 # FORMATAÇÕES DE SAÍDA DE DADOS
nome = "Edson de Oliveira"  # str()
idade = 50                  # int()
altura = 1.71               # float()
 
# FORMATACAO 1 - Usando vírgula (exibe dados de todos os tipos)
print(nome, idade, altura)
print("Nome: ",nome, "Idade: ",idade, "Altura: ",altura)
print("\tNome: ",nome, "\nIdade: ",idade, "\nAltura: ",altura)
    # para casa: pesquise os demais caracteres de \
 
# FORMATACAO 2 - Usando concatenação (+) [str()]
print(nome + str(idade) + str(altura))
 
print(type(idade))
# idade = str(idade)
print(nome + " "+ str(idade) + " " + str(altura))
print(type(idade))
 
# FORMATACAO 3 - Usando .format
print() #                                            0      1      2
print("Nome: {0} \nIdade: {1} \nAltura: {2}".format(nome, idade, altura))
 
# FORMATACAO 4 - Usando .format com álias (apelido)
print() #                                            
print("Nome: {n} \nIdade: {i} \nAltura: {a}".format(n=nome, i=idade, a=altura))
 
# FORMATACAO 5 - Usando f'print
print() #                                            
print(f"Nome: {nome} \nIdade: {idade} \nAltura: {altura}")
 
# FORMATACAO 6 - Usando TRIPLE QUOTES
print() #                                            
print(f'''
Nome: {nome}
Idade: {idade}
Altura: {altura}
''')
 
# FORMATACAO 7 - Usando o %
print() #                                            
print("Nome: %s \nIdade: %d \nAltura: %f" % (nome, idade, altura)) # %s - str() | %d - int() | %f - float
 
 
 
numero_decimal = 10 # %d - decimal | %o - octal | %x - hexadecimal
print("Decimal: %d | octal: %o | Hexadecimal: %x" % (numero_decimal, numero_decimal, numero_decimal))
 
# FORMATACAO 8 - Formatando dados numericos
 
valor1 = 55 # int()
valor2 = 34.6555 # float()
valor3 = 6688.3
valor4 = 444.44
 
print(f"""
Valor 1: {valor1}
Valor 2: {valor2}
Valor 3: {valor3}
Valor 4: {valor4}
""")
 
print(f"""
Formatacoes de numeros int():
     
Valor 1: {valor1}
Valor 1: {valor1:6d}
Valor 1: {2222:6d}
Valor 1: {222:06d}
""")
 
 
print(f"""
Valor 2: {valor2}
Valor 3: {valor3}
Valor 4: {valor4}
""")
 
print(f"""
Valor 2: {valor2:.3f}
Valor 3: {valor3:.3f}
Valor 4: {valor4:.3f}
""")
 
print(f"""
Valor 2: {valor2:10.2f}
Valor 3: {valor3:10.2f}
Valor 4: {valor4:10.2f}
""")
 
print(f"""
Saldo........: {valor2:10.2f}
Crédito......: {valor3:10.2f}
Débito.......: {valor4:10.2f}
""")
 
print(f"""
Saldo........: R$ {valor2:10.2f}
Crédito......: R$ {valor3:10.2f}
Débito.......: R$ {valor4:10.2f}
""")
