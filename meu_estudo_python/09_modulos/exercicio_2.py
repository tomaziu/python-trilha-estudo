# EXERCÍCIO: Registro de Acesso com Arquivo
# Objetivo: Aprender datetime e os

import datetime
import os

# PASSO 1: Obter data e hora atual
agora = datetime.datetime.now()
# strftime formata a data
print(f"Data atual: {agora.strftime('%d/%m/%Y %H:%M:%S')}")

# PASSO 2: Pedir nome do usuário
nome = input("Digite seu nome: ")

# PASSO 3: Criar ou adicionar no arquivo
nome_arquivo = "log.txt"

# os.path.exists() verifica se o arquivo existe
if not os.path.exists(nome_arquivo):
    # Se NÃO existe, CRIA o arquivo novo
    # 'w' = write (cria ou sobrescreve)
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(f"{agora.strftime('%d/%m/%Y %H:%M')} - {nome}\n")
    print(f"✓ Arquivo '{nome_arquivo}' criado!")
else:
    # Se JÁ existe, ADICIONA no final
    # 'a' = append (não apaga o que já tem)
    with open(nome_arquivo, "a") as arquivo:
        arquivo.write(f"{agora.strftime('%d/%m/%Y %H:%M')} - {nome}\n")
    print(f"✓ Dados adicionados ao '{nome_arquivo}'")

# PASSO 4: Listar arquivos da pasta
print("\n═══ Arquivos na pasta ═══")
# os.listdir(".") lista arquivos na pasta atual
for item in os.listdir("."):
    print(f"  📄 {item}")

# COMO FUNCIONA:
# datetime.now() → pega a data/hora do computador
# strftime() → formata: "%d/%m/%Y" = "27/06/2026"
# os.path.exists("arq.txt") → True se existe, False se não
# os.listdir(".") → ["arquivo1.py", "arquivo2.py", ...]
