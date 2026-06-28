# EXERCÍCIO: Análise de Dados com pandas
# Objetivo: Aprender a trabalhar com tabelas

import pandas as pd

# PASSO 1: Criar dados
# pandas precisa de um dicionário
dados = {
    "nome": ["Ana", "João", "Carlos", "Maria", "Pedro", "Lucia"],
    "nota": [9.0, 5.5, 7.0, 4.5, 8.5, 6.0],
    "aprovado": [True, False, True, False, True, False]
}

# PASSO 2: Criar DataFrame (tabela)
df = pd.DataFrame(dados)
print("═══ Tabela Completa ═══")
print(df)

# PASSO 3: Filtrar aprovados
# df[df["aprovado"] == True] mantém apenas linhas True
aprovados = df[df["aprovado"] == True]
print("\n═══ Apenas Aprovados ═══")
print(aprovados)

# PASSO 4: Calcular estatísticas
media_geral = df["nota"].mean()  # Média de todas as notas
media_aprovados = aprovados["nota"].mean()
print(f"\nMédia geral: {media_geral:.2f}")
print(f"Média dos aprovados: {media_aprovados:.2f}")

# PASSO 5: Salvar em CSV
# to_csv() salva como arquivo de tabela
aprovados.to_csv("resultado.csv", sep=';', index=False)
print("\n✓ Dados salvos em 'resultado.csv'")

# COMO FUNCIONA:
# pd.DataFrame(dados) → cria tabela bonita
# df[df["nota"] >= 7] → filtra linhas
# .mean() → calcula média
# .to_csv() → salva arquivo

# PANDAS É UM EXCEL EM PYTHON!
# - Filtrar: df[df["coluna"] > 5]
# - Média: df["coluna"].mean()
# - Somar: df["coluna"].sum()
# - Contar: df["coluna"].count()
