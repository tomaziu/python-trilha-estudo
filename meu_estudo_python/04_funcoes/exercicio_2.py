# EXERCÍCIO: Média com *args e **kwargs
# Objetivo: Aprender argumentos variáveis

# PASSO 1: Função com *args (aceita N argumentos)
# *args permite passar qualquer quantidade de números
# Todos ficam guardados em uma tupla chamada "args"
def media(*args):
    # sum() soma todos os números
    # len() conta quantos números foram passados
    return sum(args) / len(args)

# PASSO 2: Chamar a função com diferentes quantidades
print(f"Média de 3 números: {media(10, 7, 8):.2f}")      # 8.33
print(f"Média de 5 números: {media(9, 6, 7, 8, 10):.2f}") # 8.00
print(f"Média de 2 números: {media(5, 15):.2f}")           # 10.00

# PASSO 3: Função com **kwargs (argumentos nomeados)
# **kwargs aceita pares chave=valor
def criar_perfil(**dados):
    # .items() retorna pares (chave, valor)
    for chave, valor in dados.items():
        print(f"  {chave}: {valor}")

print("\n--- Perfil ---")
criar_perfil(nome="Ana", idade=25, cidade="SP")

# COMO FUNCIONA:
# *args: media(10, 7, 8) → args = (10, 7, 8)
# sum(args) = 25
# len(args) = 3
# 25 / 3 = 8.33

# **kwargs: criar_perfil(nome="Ana", idade=25)
# dados = {"nome": "Ana", "idade": 25}
