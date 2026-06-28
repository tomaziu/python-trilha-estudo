# EXERCÍCIO: Manipulação de Strings
# Objetivo: Aprender fatiamento e contagem

# PASSO 1: Criar uma string
nome_completo = "Maria Silva Santos"

# PASSO 2: Usar fatiamento (slicing)
# Cada letra tem um número (índice) começando do 0
# M = 0, a = 1, r = 2, i = 3, a = 4, " " = 5, S = 6...
print("Índices:")
print("  M=0, a=1, r=2, i=3, a=4, ' '=5, S=6, i=7, l=8, v=9, a=10")

# [0:6] pega do índice 0 ao 5 (6 NÃO é incluído)
print(f"\nPrimeiro nome [0:6]: {nome_completo[0:6]}")  # Maria

# [:9:-1] inverte a string a partir do índice 9
# O -1 indica que vai de trás pra frente
print(f"Sobrenome invertido: {nome_completo[:9:-1]}")

# PASSO 3: Contar letras (ignorando espaços)
contador = 0
for letra in nome_completo:
    if letra == " ":  # Se for espaço, não conta
        pass  # pass não faz nada, só pula
    else:
        contador += 1  # Adiciona 1 ao contador
    
print(f"\nQuantidade de letras (sem espaços): {contador}")

# COMO FUNCIONA O FATIAMENTO:
# nome_completo = "Maria Silva Santos"
#                  0123456789...
# [0:6] = pega de 0 até 5 = "Maria"
# [7:12] = pega de 7 até 11 = "ilva"
# [:9:-1] = inverte de 9 até 0 = "valiS"
