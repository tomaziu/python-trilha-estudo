import datetime
import os

agora = datetime.datetime.now()
print("Data e hora atual:", agora)

nome_usuario = input("Digite seu nome: ")

if not os.path.exists("log.txt"):
    with open("log.txt", "w") as arquivo_log:
        arquivo_log.write(f"{agora} - Nome do usuário: {nome_usuario}\n")
else:
    with open("log.txt", "a") as arquivo_log:
        arquivo_log.write(f"{agora} - Nome do usuário: {nome_usuario}\n")
