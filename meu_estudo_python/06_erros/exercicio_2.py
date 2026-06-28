# EXERCÍCIO: Cadastro de Alunos com Médias
# Objetivo: Aprender funções, listas e salvar em arquivo

# PASSO 1: Criar função para calcular média
def media_aluno(nota1, nota2, nota3):
    """Recebe 3 notas e retorna a média"""
    media = (nota1 + nota2 + nota3) / 3
    return media

# PASSO 2: Criar listas para cada aluno
# Cada lista guarda as 3 notas
aluno1 = []
aluno2 = []
aluno3 = []

# PASSO 3: Cadastrar notas do aluno 1
print("═══ Cadastro do Aluno 1 ═══")
while True:
    try:
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))
        # extend() adiciona vários itens de uma vez
        aluno1.extend([nota1, nota2, nota3])
        break
    except ValueError:
        print("✗ Digite um número válido (ex: 8.5)")

# PASSO 4: Cadastrar notas do aluno 2
print("\n═══ Cadastro do Aluno 2 ═══")
while True:
    try:
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))
        aluno2.extend([nota1, nota2, nota3])
        break
    except ValueError:
        print("✗ Digite um número válido (ex: 8.5)")

# PASSO 5: Cadastrar notas do aluno 3
print("\n═══ Cadastro do Aluno 3 ═══")
while True:
    try:
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))
        aluno3.extend([nota1, nota2, nota3])
        break
    except ValueError:
        print("✗ Digite um número válido (ex: 8.5)")

# PASSO 6: Calcular médias
# Chamamos a função para cada aluno
media1 = media_aluno(aluno1[0], aluno1[1], aluno1[2])
media2 = media_aluno(aluno2[0], aluno2[1], aluno2[2])
media3 = media_aluno(aluno3[0], aluno3[1], aluno3[2])

# PASSO 7: Salvar em arquivo
# 'w' = write (apaga tudo e reescreve)
# with abre e fecha o arquivo automaticamente
with open("medias_alunos.txt", "w") as arquivo:
    arquivo.write(f"Média do Aluno 1: {media1:.2f}\n")
    arquivo.write(f"Média do Aluno 2: {media2:.2f}\n")
    arquivo.write(f"Média do Aluno 3: {media3:.2f}\n")

# PASSO 8: Mostrar na tela
print("\n═══ RESULTADOS ═══")
print(f"Aluno 1: Notas {aluno1} → Média: {media1:.2f}")
print(f"Aluno 2: Notas {aluno2} → Média: {media2:.2f}")
print(f"Aluno 3: Notas {aluno3} → Média: {media3:.2f}")
print("\n✓ Dados salvos em 'medias_alunos.txt'")

# COMO FUNCIONA:
# aluno1 = [8.0, 7.0, 9.0]
# media_aluno(8.0, 7.0, 9.0) = (8+7+9)/3 = 8.0
# O arquivo recebe: "Média do Aluno 1: 8.00"
