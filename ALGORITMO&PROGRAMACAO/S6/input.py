#---------------------------------------------------------#

#S6-1

# Solicita a lista de palavras
palavras = input("Digite a lista de palavras: ")

# Converte a entrada para uma lista de strings
lista_palavras = eval(palavras)

# Exibe as palavras que têm 4 letras
for palavra in lista_palavras:
    if len(palavra) == 4:
        print(palavra)

#S6-2

# Exibe os números de 0 a 9
for i in range(10):
    print(i)

# Exibe os números de 0 a 1
for i in range(2):
    print(i)

#S6-3

# Inteiros de 3 até 12
for i in range(3, 13):
    print(i)

# Inteiros de 0 até (mas não incluindo) 9, com passo de 2
for i in range(0, 9, 2):
    print(i)

# Inteiros de 0 até (mas não incluindo) 24, com passo de 3
for i in range(0, 24, 3):
    print(i)

# Inteiros de 3 até (mas não incluindo) 12, com passo de 5
for i in range(3, 12, 5):
    print(i)

#---------------------------------------------------------#
