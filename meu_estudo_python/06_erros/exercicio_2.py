aluno1 = []
aluno2 = []
aluno3 = []

def media_aluno(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

print("Digite as notas do aluno 1:")
while True:
    try:
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))
        aluno1.append(nota1)
        aluno1.append(nota2)
        aluno1.append(nota3)
        break
    except ValueError:
        print("Por favor, digite um número válido.")

print("Digite as notas do aluno 2:")
while True:
    try:
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))
        aluno2.append(nota1)
        aluno2.append(nota2)
        aluno2.append(nota3)
        break
    except ValueError:
        print("Por favor, digite um número válido.")

print("Digite as notas do aluno 3:")
while True:
    try:
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))
        aluno3.append(nota1)
        aluno3.append(nota2)
        aluno3.append(nota3)
        break
    except ValueError:
        print("Por favor, digite um número válido.")

media1 = media_aluno(aluno1[0], aluno1[1], aluno1[2])
media2 = media_aluno(aluno2[0], aluno2[1], aluno2[2])
media3 = media_aluno(aluno3[0], aluno3[1], aluno3[2])

with open ("medias_alunos.txt", "w") as arquivo:
    arquivo.write(f"A média do aluno 1 é: {media1:.2f}\n")
    arquivo.write(f"A média do aluno 2 é: {media2:.2f}\n")
    arquivo.write(f"A média do aluno 3 é: {media3:.2f}\n")

print(f"A média do aluno 1 é: {media1:.2f}")
print(f"A média do aluno 2 é: {media2:.2f}")
print(f"A média do aluno 3 é: {media3:.2f}")

