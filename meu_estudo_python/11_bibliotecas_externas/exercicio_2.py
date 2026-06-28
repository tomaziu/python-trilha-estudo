import pandas as pd

dados = {
    "nome": ["Ana", "João", "Carlos", "Maria", "Pedro"],
    "nota": [9, 5, 7, 4, 8],
    "aprovado": [True, False, True, False, True]
}

df = pd.DataFrame(dados)

df_aprovados = df[df["aprovado"] == True]

print(df_aprovados)

media_notas = df_aprovados["nota"].mean()
print("Média das notas:", media_notas)

df_aprovados.to_csv("resultado.csv", sep=';', index=False)