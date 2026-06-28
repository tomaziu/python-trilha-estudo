# EXERCÍCIO: Gerador de Senhas
# Objetivo: Aprender a usar módulos (random, math)

# PASSO 1: Importar funções dos módulos
# from importa funções específicas
from random import choice, randint
from math import sqrt

# PASSO 2: Criar função para gerar senha
def gerar_senha(tamanho=8):
    """Gera senha aleatória"""
    # Caracteres permitidos na senha
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%"
    senha = ""
    
    for _ in range(tamanho):  # Repete 'tamanho' vezes
        # choice() escolhe UM caractere aleatório da string
        senha += choice(caracteres)
    
    return senha

# PASSO 3: Testar a função
print("═══ Gerador de Senhas ═══")
senha1 = gerar_senha(8)
senha2 = gerar_senha(12)
print(f"Senha 8 caracteres: {senha1}")
print(f"Senha 12 caracteres: {senha2}")

# PASSO 4: Outros usos dos módulos
print("\n═══ Outros Exemplos ═══")

# randint gera número aleatório entre a e b
numero_sorteado = randint(1, 100)
print(f"Número sorteado (1-100): {numero_sorteado}")

# choice escolhe item de uma lista
frutas = ["maçã", "banana", "laranja", "uva"]
fruta_escolhida = choice(frutas)
print(f"Fruta sorteada: {fruta_escolhida}")

# sqrt calcula raiz quadrada
raiz = sqrt(144)
print(f"Raiz de 144 = {raiz}")

# COMO FUNCIONA:
# choice("ABC") → pode retornar "A", "B" ou "C"
# randint(1, 10) → retorna número entre 1 e 10
# sqrt(144) → retorna 12.0
