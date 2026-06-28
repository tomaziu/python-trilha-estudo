nome_completo = "Thomaz de Morais Nunes"

print(f"Primeiro nome: {nome_completo[0:6]}")
print(f"Sobrenome invertido: {nome_completo[:9:-1]}")

contador = 0
for letra in nome_completo:
    if letra == " ":
        pass
    else:
        contador += 1
    
print(f"Quantidade: {contador}")
