def soma2D(t, s):
    for i in range(len(t)):
        for j in range(len(t[i])):
            t[i][j] += s[i][j]

# exemplos d dados
t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
s = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]]

soma2D(t, s)

for linha in t:
    print(linha)
