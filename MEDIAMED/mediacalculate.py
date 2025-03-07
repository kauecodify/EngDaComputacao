# armazena as notas de cada disciplina
disciplinas = {
    "Algoritmo e Programação de Computadores": [],
    "Cálculo I": [],
    "Cálculo II": [],
    "Introdução à Computação": []
}

# adiciona notas
def adicionar_notas():
    print("\n--- Adicionar Notas ---")
    semana = input("Digite o número da semana (ex: S1, S2, etc.): ")
    for disciplina in disciplinas:
        nota = float(input(f"Digite a nota de {disciplina} para a {semana}: "))
        disciplinas[disciplina].append(nota)
    print("Notas adicionadas com sucesso!\n")

# calcula a média ponderada de uma disciplina
def calcular_media_ponderada(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

# exibe as médias
def exibir_medias():
    print("\n--- Médias Finais ---")
    media_geral = 0
    for disciplina, notas in disciplinas.items():
        media = calcular_media_ponderada(notas)
        print(f"{disciplina}: {media:.2f}")
        media_geral += media
    media_geral /= len(disciplinas)
    print(f"\nMédia Geral: {media_geral:.2f}\n")

# menu
while True:
    print("1 - Adicionar notas de uma semana")
    print("2 - Calcular médias e exibir resultados")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_notas()
    elif opcao == "2":
        exibir_medias()
    elif opcao == "3":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.\n")

# rodar com tecla F5 :D