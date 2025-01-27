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