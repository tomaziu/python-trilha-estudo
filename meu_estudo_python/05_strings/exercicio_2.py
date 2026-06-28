# EXERCÍCIO: Inverter Palavras e Contar
# Objetivo: Aprender split(), join() e loops em strings

# PASSO 1: Pedir frase ao usuário
frase = input("Digite uma frase: ")

# PASSO 2: Dividir a frase em palavras
# split(" ") divide onde tem espaço
# "Olá Mundo" vira ["Olá", "Mundo"]
frase_cortada = frase.split(" ")
print(f"Palavras: {frase_cortada}")

# PASSO 3: Inverter cada palavra
invertidas = []
for palavra in frase_cortada:
    # [::-1] inverte a string
    # "Olá" vira "aló"
    invertidas.append(palavra[::-1])

print(f"Palavras invertidas: {invertidas}")

# PASSO 4: Juntar de volta em frase
# join() junta a lista com um separador
# " ".join(["aló", "odnuM"]) = "aló odnuM"
print(f"Frase invertida: {' '.join(invertidas)}")

# PASSO 5: Contar palavras grandes
contador = 0
for palavra in frase_cortada:
    if len(palavra) > 5:  # len() retorna o tamanho
        contador += 1

print(f"\nPalavras com mais de 5 letras: {contador}")

# COMO FUNCIONA:
# split(" ") → ["Olá", "Mundo", "Python"]
# [::-1] → inverte: "aló", "odnuM", "nohtyP"
# join(" ") → "aló odnuM nohtyP"
# len("Python") = 6 → 6 > 5 = True → conta
