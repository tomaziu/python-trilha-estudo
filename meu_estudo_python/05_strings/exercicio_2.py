frase = input("Digite uma frase: ")

frase_cortada = frase.split(" ")
invertidas = []

for palavra in frase_cortada:
    invertidas.append(palavra[::-1])

print(f"Frase invertida: {' '.join(invertidas)}")

contador = 0
for palavra in frase_cortada:
    if len(palavra) > 5:
        contador += 1

print(f"Quantidade de palavras com mais de 5 caracteres: {contador}")