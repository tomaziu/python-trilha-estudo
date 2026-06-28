# EXERCÍCIO: Escopo Local vs Global
# Objetivo: Entender onde as variáveis existem

# PASSO 1: Criar função com variável local
def contagem(num):
    # variavel_local é LOCAL - só existe DENTRO da função
    # Quando a função termina, ela some
    variavel_local = 1
    while variavel_local <= num:
        print(variavel_local)
        variavel_local += 1
    
# PASSO 2: Chamar a função
print("--- Chamando contagem(3) ---")
contagem(3)

# PASSO 3: Criar variável global (fora da função)
# Esta variavel_local é DIFERENTE da da função
# Ela só existe AQUI fora
variavel_local = 10

print(f"\nVariável global: {variavel_local}")  # 10

# A variável da função (1, 2, 3) já sumiu
# Esta variavel_local = 10 é outra coisa completamente diferente

# REGRAS DO ESCOPO:
# 1. Variável dentro de função = LOCAL (morre quando a função termina)
# 2. Variável fora de função = GLOBAL (existe enquanto o programa roda)
# 3. Mesmo nome, variáveis diferentes!

# EXEMPLO VISUAL:
# ┌─────────────────────────┐
# │ GLOBAL (fora)           │
# │ variavel_local = 10     │
# │                         │
# │ ┌─────────────────────┐ │
# │ │ LOCAL (dentro)      │ │
# │ │ variavel_local = 1  │ │
# │ │ (só existe aqui)    │ │
# │ └─────────────────────┘ │
# └─────────────────────────┘
