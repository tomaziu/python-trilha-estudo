# EXERCÍCIO: Listas com Comprehension
# Objetivo: Aprender a criar listas em uma linha

# PASSO 1: Lista de frases com espaços extras
frases = ["  Olá Mundo  ", "Python é legal", "  code  ", "Aprender Python"]

# ANTES (sem comprehension) - 4 linhas:
# resultado = []
# for frase in frases:
#     resultado.append(frase.strip())

# DEPOIS (com comprehension) - 1 linha:
# [expressão for item in lista]
sem_espaco = [frase.strip() for frase in frases]
print("Sem espaços:", sem_espaco)

# PASSO 2: Filtrar por tamanho
# [expressão for item in lista if condição]
grandes = [frase for frase in sem_espaco if len(frase) > 10]
print("Mais de 10 letras:", grandes)

# PASSO 3: Exemplo com números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar apenas pares
pares = [n for n in numeros if n % 2 == 0]
print("\nNúmeros pares:", pares)

# Dobrar os pares
dobros = [n * 2 for n in numeros if n % 2 == 0]
print("Dobro dos pares:", dobros)

# Quadrado de todos
quadrados = [n ** 2 for n in numeros]
print("Quadrados:", quadrados)

# COMO FUNCIONA:
# [n for n in [1,2,3]] → [1, 2, 3]
# [n for n in [1,2,3] if n > 1] → [2, 3]
# [n * 2 for n in [1,2,3]] → [2, 4, 6]

# É um atalho para o loop:
# resultado = []
# for n in numeros:
#     if n % 2 == 0:
#         resultado.append(n * 2)
