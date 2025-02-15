import tkinter as tk
from tkinter import messagebox
import itertools

# calcular A → B
def implies(A, B):
    return not A or B

# calcular ¬(A ∨ B)
def not_or(A, B):
    return not (A or B)

# calcular a proposição (A → B) ∧ [¬(A ∨ B)]
def proposition_1(A, B):
    return implies(A, B) and not_or(A, B)

# calcular A ∧ (B ∨ C)
def proposition_2(A, B, C):
    return A and (B or C)

# calcular (A ∧ B) ∨ (A ∧ C)
def proposition_3(A, B, C):
    return (A and B) or (A and C)

# calcular A → (B → A)
def proposition_4(A, B):
    return implies(A, implies(B, A))

# gerar a Tabela Verdade para a proposição (A → B) ∧ [¬(A ∨ B)]
def generate_proposition_1():
    values = list(itertools.product([False, True], repeat=2))
    table_1 = []
    for A, B in values:
        table_1.append((A, B, proposition_1(A, B)))
    return table_1

#  gerar a Tabela Verdade para A ∧ (B ∨ C) ⇔ (A ∧ B) ∨ (A ∧ C)
def generate_proposition_2():
    values = list(itertools.product([False, True], repeat=3))
    table_2 = []
    for A, B, C in values:
        table_2.append((A, B, C, proposition_2(A, B, C) == proposition_3(A, B, C)))
    return table_2

# gerar a Tabela Verdade para A → (B → A)
def generate_proposition_3():
    values = list(itertools.product([False, True], repeat=2))
    table_3 = []
    for A, B in values:
        table_3.append((A, B, proposition_4(A, B)))
    return table_3

# mostrar as Tabelas Verdade nas Labels
def show_truth_tables(table_number):
    if table_number == 1:
        table_1 = generate_proposition_1()
        text = "Tabela Verdade para (A → B) ∧ [¬(A ∨ B)]\n"
        text += "A B | (A → B) ∧ [¬(A ∨ B)]\n"
        for row in table_1:
            text += f"{row[0]} {row[1]} | {row[2]}\n"
    
    elif table_number == 2:
        table_2 = generate_proposition_2()
        text = "Tabela Verdade para A ∧ (B ∨ C) ⇔ (A ∧ B) ∨ (A ∧ C)\n"
        text += "A B C | A ∧ (B ∨ C) ⇔ (A ∧ B) ∨ (A ∧ C)\n"
        for row in table_2:
            text += f"{row[0]} {row[1]} {row[2]} | {row[3]}\n"
    
    elif table_number == 3:
        table_3 = generate_proposition_3()
        text = "Tabela Verdade para A → (B → A)\n"
        text += "A B | A → (B → A)\n"
        for row in table_3:
            text += f"{row[0]} {row[1]} | {row[2]}\n"
    
    label_tables.config(text=text)

# Criando a interface gráfica
root = tk.Tk()
root.title("Tabelas Verdade")

# Label para exibir as tabelas verdade
label_tables = tk.Label(root, text="", justify="left", font=("Arial", 10), width=50, height=20)
label_tables.pack(padx=10, pady=10)

# Botão para gerar e exibir a Tabela Verdade 1
button_show_table_1 = tk.Button(root, text="Mostrar Tabela Verdade 1", command=lambda: show_truth_tables(1))
button_show_table_1.pack(padx=10, pady=5)

# Botão para gerar e exibir a Tabela Verdade 2
button_show_table_2 = tk.Button(root, text="Mostrar Tabela Verdade 2", command=lambda: show_truth_tables(2))
button_show_table_2.pack(padx=10, pady=5)

# Botão para gerar e exibir a Tabela Verdade 3
button_show_table_3 = tk.Button(root, text="Mostrar Tabela Verdade 3", command=lambda: show_truth_tables(3))
button_show_table_3.pack(padx=10, pady=5)

# Rodando a interface gráfica
root.mainloop()
