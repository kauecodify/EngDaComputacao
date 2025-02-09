# semana 1 - Exercício 2. Cap. 3

soma = 0

for i in range (1, 101):
    soma += i
print(f"a soma dos cem primeiros números naturais é: {soma}")

# semana 1 - Exercício 2. Cap. 4 – Ex 3c

N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))
N3 = float(input("Digite a terceira nota: "))
N4 = float(input("Digite a quarta nota: "))

media = (N1 + N2 + N3 + N4) / 4

if media >=5:
    print(f"aprovado com média: {media:.2f}")
else:
    print(f"reprovado co média: {media:.2f}")

# SEMANA 1 - Exercício 1 - Cap. 3 - Ex 4a

celsius = float(input("Digite a temperatura em graus celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print( ("A temperatura em fahrenheit é: {fahrenheit:.2f}ºF"))

# SEMANA 1 - EXERCÍCIO 2.6 - LISTA DE PALAVRAS

palavras = [ 'taco,', 'bola', 'celeiro', 'cesta', 'peteca']

primeira_palavra = min(palavras) #bola
ultima_palavra = max(palavras) #taco

print(f"A primeira palavra em ordem alfabética é : {primeira_palavra}")
print(f"A última palavra em ordem alfabética é: {ultima_palavra}")