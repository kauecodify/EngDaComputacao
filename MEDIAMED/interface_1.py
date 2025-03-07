import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import pandas as pd

disciplinas = {
    "Algoritmo e Programação de Computadores": [],
    "Cálculo I": [],
    "Cálculo II": [],
    "Introdução à Computação": []
}

def adicionar_notas():
    semana = entrada_semana.get()
    if not semana:
        messagebox.showerror("Erro", "Digite o número da semana!")
        return

    for disciplina in disciplinas:
        nota = entrada_notas[disciplina].get()
        if nota:
            try:
                nota = float(nota)
                disciplinas[disciplina].append((semana, nota))
                entrada_notas[disciplina].delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Erro", f"Nota inválida para {disciplina}!")
        else:
            messagebox.showerror("Erro", f"Digite a nota para {disciplina}!")
            return

    messagebox.showinfo("Sucesso", "Notas adicionadas com sucesso!")
    entrada_semana.delete(0, tk.END)

def exibir_medias():
    resultado = "--- Médias Finais ---\n"
    media_geral = 0
    for disciplina, notas in disciplinas.items():
        if notas:
            media = sum(nota for _, nota in notas) / len(notas)
            resultado += f"{disciplina}: {media:.2f}\n"
            media_geral += media
        else:
            resultado += f"{disciplina}: 0.00\n"
    media_geral /= len(disciplinas)
    resultado += f"\nMédia Geral: {media_geral:.2f}"
    messagebox.showinfo("Resultados", resultado)

def apagar_dados_semana():
    semana = entrada_apagar_semana.get()
    if not semana:
        messagebox.showerror("Erro", "Digite o número da semana!")
        return

    for disciplina in disciplinas:
        disciplinas[disciplina] = [(s, nota) for s, nota in disciplinas[disciplina] if s != semana]

    messagebox.showinfo("Sucesso", f"Dados da semana {semana} apagados com sucesso!")
    entrada_apagar_semana.delete(0, tk.END)

def criar_planilha():

    dados = {}
    for disciplina, notas in disciplinas.items():
        dados[disciplina] = {semana: nota for semana, nota in notas}

    # DataFrame
    df = pd.DataFrame(dados).fillna("-")
    df.index.name = "Semana"

    df["Média"] = df.mean(axis=1, numeric_only=True).round(2)

    for row in tabela.get_children():
        tabela.delete(row)

    for semana, row in df.iterrows():
        valores = [semana] + [row[disciplina] for disciplina in df.columns]
        tabela.insert("", "end", values=valores)

    messagebox.showinfo("Sucesso", "Planilha exibida na interface!")

# interface gráfica
janela = tk.Tk()
janela.title("Cálculo de Médias")
janela.geometry("600x500")
janela.configure(bg="#ffcccc")

try:
    imagem_fundo = Image.open("fundo.png") 
    imagem_fundo = imagem_fundo.resize((700, 600), Image.ANTIALIAS)
    imagem_fundo = ImageTk.PhotoImage(imagem_fundo)
    fundo_label = tk.Label(janela, image=imagem_fundo)
    fundo_label.place(relwidth=1, relheight=1)
except FileNotFoundError:
    print("Imagem de fundo não encontrada. Continuando sem imagem.")

estilo = ttk.Style()
estilo.configure("TButton", font=("Arial", 10), background="#ff0000", foreground="black", borderwidth=0)
estilo.configure("TEntry", font=("Arial", 10), background="#ffffff", borderwidth=2, relief="solid")

estilo.configure("Treeview", background="#ffffff", foreground="#000000", fieldbackground="#ffffff", font=("Arial", 10))
estilo.configure("Treeview.Heading", background="#ff0000", foreground="gray", font=("Arial", 12, "bold"))
estilo.map("Treeview", background=[("selected", "#ff6666")])

tk.Label(janela, text="Semana (ex: S1, S2):", bg="#ffcccc", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
entrada_semana = ttk.Entry(janela)
entrada_semana.grid(row=0, column=1, padx=10, pady=5)

entrada_notas = {}
for i, disciplina in enumerate(disciplinas, start=1):
    tk.Label(janela, text=f"{disciplina}:", bg="#ffcccc", font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5)
    entrada_notas[disciplina] = ttk.Entry(janela)
    entrada_notas[disciplina].grid(row=i, column=1, padx=10, pady=5)

ttk.Button(janela, text="Adicionar Notas", command=adicionar_notas).grid(row=5, column=0, padx=10, pady=10)
ttk.Button(janela, text="Calcular Médias", command=exibir_medias).grid(row=5, column=1, padx=10, pady=10)

tk.Label(janela, text="Apagar dados da semana:", bg="#ffcccc", font=("Arial", 12)).grid(row=6, column=0, padx=10, pady=5)
entrada_apagar_semana = ttk.Entry(janela)
entrada_apagar_semana.grid(row=6, column=1, padx=10, pady=5)
ttk.Button(janela, text="Apagar", command=apagar_dados_semana).grid(row=7, column=1, padx=10, pady=10)

ttk.Button(janela, text="Exibir Planilha", command=criar_planilha).grid(row=8, column=0, columnspan=2, padx=10, pady=10)

colunas = ["Semana"] + list(disciplinas.keys()) + ["Média"]
tabela = ttk.Treeview(janela, columns=colunas, show="headings")
for col in colunas:
    tabela.heading(col, text=col)
tabela.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

janela.mainloop()